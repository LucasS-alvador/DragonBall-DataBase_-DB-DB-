import os
import sys

# Add project root to path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.app import app
from src.model.raca import Raca
from src.model.obra import Obra
from src.model.personagembase import PersonagemBase
from sqlalchemy import text

def cleanup_duplicates(Model, name_field='nome', references=None):
    """
    Generic function to clean up duplicates in any table
    Model: SQLAlchemy model class
    name_field: field to check for duplicates
    references: list of tuples (table_name, fk_field) that reference this model
    """
    items = Model.query.all()
    seen = {}
    duplicates = []
    
    # Find duplicates
    for item in items:
        name = getattr(item, name_field)
        if name in seen:
            duplicates.append(item.id)
        else:
            seen[name] = item.id
    
    if duplicates:
        # Update references to use the first instance
        if references:
            for duplicate_id in duplicates:
                original_id = seen[getattr(Model.query.get(duplicate_id), name_field)]
                for table_name, fk_field in references:
                    app.db.session.execute(
                        text(f'UPDATE {table_name} SET {fk_field} = :original WHERE {fk_field} = :duplicate'),
                        {'original': original_id, 'duplicate': duplicate_id}
                    )
        
        # Delete duplicates
        for duplicate_id in duplicates:
            app.db.session.execute(
                text(f'DELETE FROM {Model.__tablename__} WHERE id = :id'),
                {'id': duplicate_id}
            )
    
    return len(duplicates)

def cleanup_characters():
    """Clean up character entries with same name but different data"""
    characters = PersonagemBase.query.all()
    seen = {}
    duplicates = []
    
    for char in characters:
        if char.nome in seen:
            # Keep the one with more complete data (has description)
            existing = PersonagemBase.query.get(seen[char.nome])
            if not existing.descricao and char.descricao:
                # This one has more data, delete the other one
                duplicates.append(existing.id)
                seen[char.nome] = char.id
            else:
                # Keep the existing one
                duplicates.append(char.id)
        else:
            seen[char.nome] = char.id
    
    # Delete duplicates
    for duplicate_id in duplicates:
        app.db.session.execute(
            text('DELETE FROM PersonagemBase WHERE id = :id'),
            {'id': duplicate_id}
        )
    
    return len(duplicates)

def cleanup():
    with app.app_context():
        # Clean up races
        races_removed = cleanup_duplicates(
            Raca, 
            references=[('PersonagemBase', 'raca_id')]
        )
        
        # Clean up works
        obras_removed = cleanup_duplicates(
            Obra,
            references=[('Saga', 'obra_id')]
        )
        
        # Clean up characters with same name
        chars_removed = cleanup_characters()
        
        # Commit all changes
        app.db.session.commit()
        
        return races_removed, obras_removed, chars_removed

if __name__ == '__main__':
    try:
        races, obras, chars = cleanup()
        print(f"Cleanup completed successfully!")
        print(f"Removed {races} duplicate races")
        print(f"Removed {obras} duplicate works")
        print(f"Removed {chars} duplicate characters")
    except Exception as e:
        print(f"Error during cleanup: {str(e)}")
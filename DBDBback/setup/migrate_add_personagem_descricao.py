import os
import sys

# Add project root to path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.app import app
from src.database import db
from sqlalchemy import text

def migrate():
    with app.app_context():
        db.session.execute(text('''
            ALTER TABLE PersonagemBase 
            ADD COLUMN descricao VARCHAR(512);
        '''))
        db.session.commit()

if __name__ == '__main__':
    try:
        migrate()
        print("Migration completed successfully!")
    except Exception as e:
        print(f"Error during migration: {str(e)}")
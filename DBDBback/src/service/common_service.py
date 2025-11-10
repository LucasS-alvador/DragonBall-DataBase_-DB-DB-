from database import db
from datetime import datetime, date

# --- create

def create_object(m_class, **kwargs):
    try:
        # Converter datas se string
        date_fields = ['dataNasc', 'dataMorte', 'dtIni', 'dtFim']
        for key, value in kwargs.items():
            if key in date_fields and value:
                if isinstance(value, str):
                    try:
                        kwargs[key] = datetime.strptime(value, '%Y-%m-%d').date()
                    except ValueError as e:
                        raise ValueError(f"Formato de data inválido para {key}. Use YYYY-MM-DD, recebido: {value}")
                elif not isinstance(value, date):
                    raise ValueError(f"Valor inválido para {key}. Deve ser uma string no formato YYYY-MM-DD ou um objeto date.")
        
        # Validar campos obrigatórios se o modelo tiver a lista
        if hasattr(m_class, 'required_fields'):
            missing_fields = [field for field in m_class.required_fields if field not in kwargs]
            if missing_fields:
                raise ValueError(f"Campos obrigatórios ausentes: {', '.join(missing_fields)}")
        
        # Validar valores numéricos
        for key, value in kwargs.items():
            if key in ['epIni', 'epFim', 'poderBase', 'poderMult', 'limMinutos']:
                try:
                    if not isinstance(value, (int, float)):
                        value = float(value) if '.' in str(value) else int(value)
                    kwargs[key] = value
                    if value < 0:
                        raise ValueError(f"O campo {key} não pode ser negativo")
                except (ValueError, TypeError):
                    raise ValueError(f"Valor inválido para {key}: {value}. Deve ser um número.")
        
        # Criar objeto
        obj = m_class(**kwargs)
        
        # Validar regras específicas do modelo
        if hasattr(obj, 'validate'):
            obj.validate()
        
        # Salvar no banco
        db.session.add(obj)
        db.session.commit()
        db.session.refresh(obj)
        return obj
        
    except ValueError as e:
        db.session.rollback()
        print(f"[SERVICE] Erro de validação ao criar {m_class.__name__}: {str(e)}")
        raise
        
    except Exception as e:
        db.session.rollback()
        print(f"[SERVICE] Erro ao criar {m_class.__name__}: {str(e)}")
        raise

# --- get

def get_objects(m_class):
    return db.session.query(m_class).all()
        
def get_object_by_attribute(m_class, attribute, value):
    # Clear any stale session state
    db.session.remove()
    
    # Get object in fresh session
    with db.session.begin():
        return db.session.query(m_class).filter(getattr(m_class, attribute) == value).first()

# --- delete

def delete_object_by_id(m_class, object_id):
    try:
        obj = db.session.query(m_class).filter(m_class.id == object_id).first()
        if not obj:
            print(f"[SERVICE] Objeto {m_class.__name__} com ID {object_id} não encontrado para deleção")
            return False
        
        print(f"[SERVICE] Deletando {m_class.__name__} com ID {object_id}")
        db.session.delete(obj)
        db.session.commit()
        return True
    
    except Exception as e:
        print(f"[SERVICE] Erro ao deletar {m_class.__name__} com ID {object_id}: {str(e)}")
        db.session.rollback()
        return False

# delete by the object itself
def delete_object(obj):
    try:
        if not obj:
            print(f"[SERVICE] Objeto não encontrado para deleção")
            return False
        
        # Guardar referência da classe e ID
        obj_class = type(obj)
        obj_id = obj.id

        # Re-load object in the current session to ensure it's attached
        print(f"[SERVICE] Deletando objeto {obj_class.__name__} com ID {obj_id}")
        target = db.session.get(obj_class, obj_id)
        if not target:
            print(f"[SERVICE] Objeto {obj_class.__name__} com ID {obj_id} não encontrado (já removido?)")
            return False

        # Deletar e commitar
        db.session.delete(target)
        db.session.commit()

        # Verify deletion by trying to load again
        verify = db.session.get(obj_class, obj_id)
        if verify is not None:
            print(f"[SERVICE] Objeto ainda existe após deleção")
            return False
        
        print(f"[SERVICE] Objeto deletado com sucesso")
        return True
    
    except Exception as e:
        print(f"[SERVICE] Erro ao deletar objeto: {str(e)}")
        db.session.rollback()
        return False
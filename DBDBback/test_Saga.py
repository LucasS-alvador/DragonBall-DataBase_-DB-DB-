import pytest
import os
from flask import Flask
from database import db
from service.common_service import create_object, get_object_by_attribute, delete_object
from model.obra import Obra
from model.saga import Saga
from model.personagemsaga import PersonagemSaga
from model.personagembase import PersonagemBase
from model.raca import Raca
from datetime import date
from warnings import warn

# Criar app para testes com banco de dados em memória
app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'TESTING': True
})

# Inicializar banco de dados
db.init_app(app)

# Criar tabelas no banco de dados de teste
with app.app_context():
    db.create_all()
    
# Garantir que o banco está vazio
    try:
        db.session.query(Saga).delete()
        db.session.query(Obra).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao limpar banco de dados: {e}")

@pytest.fixture
def setup_database():
    with app.app_context():
        # Limpar dados de testes anteriores se existirem
        obra = get_object_by_attribute(Obra, "nome", "Obra com Saga")
        if obra:
            delete_object(obra)

        obra = get_object_by_attribute(Obra, "nome", "Cascade Obra")
        if obra:
            delete_object(obra)
        
        yield
        
        # Limpar após os testes
        obra = get_object_by_attribute(Obra, "nome", "Obra com Saga")
        if obra:
            delete_object(obra)
            
        obra = get_object_by_attribute(Obra, "nome", "Cascade Obra")
        if obra:
            delete_object(obra)

def test_create_saga(setup_database):
    with app.app_context():
        # Criar a Obra pai
        obra = create_object(
            Obra,
            nome="Obra com Saga",
            dtIni=date(2023, 1, 1),
            dtFim=date(2023, 12, 31),
            imagem="http://example.com/saga.png"
        )

        # Criar a Saga vinculada à Obra
        saga = create_object(
            Saga,
            desc="Saga Teste",
            epIni=1,
            epFim=12,
            obra_id=obra.id,
            imagem="http://example.com/saga_img.png"
        )

        assert saga.id is not None
        assert saga.desc == "Saga Teste"
        assert saga.epIni == 1
        assert saga.epFim == 12
        assert saga.obra_id == obra.id
        assert saga.imagem == "http://example.com/saga_img.png"

def test_create_saga_validation(setup_database):
    with app.app_context():
        # Criar a Obra pai
        obra = create_object(
            Obra,
            nome="Obra com Saga",
            dtIni=date(2023, 1, 1),
            dtFim=date(2023, 12, 31),
            imagem="http://example.com/saga.png"
        )

        # Testar validação de episódios
        with pytest.raises(ValueError, match="O episódio final.*deve ser maior ou igual ao inicial"):
            create_object(
                Saga,
                desc="Saga Inválida",
                epIni=10,
                epFim=5,
                obra_id=obra.id
            )

        # Testar validação de episódio inicial
        with pytest.raises(ValueError, match="O episódio inicial.*deve ser maior que zero"):
            create_object(
                Saga,
                desc="Saga Inválida",
                epIni=0,
                epFim=5,
                obra_id=obra.id
            )

        # Testar validação de obra inexistente
        with pytest.raises(ValueError, match="Obra com ID.*não encontrada"):
            create_object(
                Saga,
                desc="Saga Inválida",
                epIni=1,
                epFim=5,
                obra_id=9999
            )

        # Testar validação de descrição vazia
        with pytest.raises(ValueError, match="A descrição não pode estar vazia"):
            create_object(
                Saga,
                desc="",
                epIni=1,
                epFim=5,
                obra_id=obra.id
            )

def test_get_saga(setup_database):
    with app.app_context():
        # Criar obra e saga para teste
        obra = create_object(
            Obra,
            nome="Obra com Saga",
            dtIni=date(2023, 1, 1),
            dtFim=date(2023, 12, 31),
            imagem="http://example.com/saga.png"
        )
        
        create_object(
            Saga,
            desc="Saga Teste",
            epIni=1,
            epFim=12,
            obra_id=obra.id
        )
        
        # Buscar e verificar
        saga = get_object_by_attribute(Saga, "desc", "Saga Teste")
        assert saga is not None
        assert saga.desc == "Saga Teste"
        assert saga.obra is not None
        assert saga.obra.nome == "Obra com Saga"

def test_delete_saga(setup_database):
    with app.app_context():
        # Criar obra e saga para teste
        obra = create_object(
            Obra,
            nome="Obra com Saga",
            dtIni=date(2023, 1, 1),
            dtFim=date(2023, 12, 31),
            imagem="http://example.com/saga.png"
        )
        
        saga = create_object(
            Saga,
            desc="Saga Teste",
            epIni=1,
            epFim=12,
            obra_id=obra.id
        )
        
        # Deletar e verificar
        ok = delete_object(saga)
        assert ok is True

        # Confirmar que foi removida
        saga = get_object_by_attribute(Saga, "desc", "Saga Teste")
        assert saga is None

def test_cascade_delete_with_obra(setup_database):
    with app.app_context():
        # Criar Obra + Saga
        obra = create_object(
            Obra,
            nome="Cascade Obra",
            dtIni=date(2022, 1, 1),
            dtFim=date(2022, 6, 1),
            imagem=""
        )

        saga = create_object(
            Saga,
            desc="Cascade Saga",
            epIni=5,
            epFim=10,
            obra_id=obra.id
        )

        # Deletar Obra (deve cascatear para Saga)
        delete_object(obra)
        
        # Saga deve ter sido removida
        deleted_saga = get_object_by_attribute(Saga, "desc", "Cascade Saga")
        assert deleted_saga is None

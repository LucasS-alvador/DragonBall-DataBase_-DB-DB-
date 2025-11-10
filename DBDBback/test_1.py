# tests/test_models.py
import pytest
from datetime import date
from warnings import warn

from config import app, db
from service.common_service import create_object, get_object_by_attribute, delete_object, get_objects

from model.raca import Raca
from model.obra import Obra
from model.saga import Saga
from model.personagembase import PersonagemBase
from model.personagemsaga import PersonagemSaga
from model.transformacao import Transformacao

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Recreate the database for test isolation"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


def test_create_raca():
    with app.app_context():
        raca = create_object(
            Raca,
            nome='Humano',
            cor='Pele clara',
            desc='Descrição da raça humana',
            poderBase=10,
            imagem='http://example.com/raca.png'
        )
        assert raca.id is not None
        assert isinstance(raca.id, int)
        assert raca.nome == "Humano"
        assert raca.desc == "Descrição da raça humana"


def test_create_obra_and_saga():
    with app.app_context():
        obra = create_object(
            Obra,
            nome="Dragon Ball Z",
            dtIni=date(1989, 4, 26),
            dtFim=date(1996, 1, 31),
            imagem="http://example.com/dbz.png"
        )
        saga = create_object(
            Saga,
            desc="Saga dos Sayajins",
            epIni=1,
            epFim=35,
            obra_id=obra.id
        )
        assert saga.obra.nome == "Dragon Ball Z"


def test_create_personagembase_and_personagemsaga():
    with app.app_context():
        raca = get_object_by_attribute(Raca, "nome", "Humano")
        saga = get_object_by_attribute(Saga, "desc", "Saga dos Sayajins")

        goku_base = create_object(
            PersonagemBase,
            nome="Goku",
            dataNasc=date(737, 4, 16),
            sexo="Masculino",
            imagem="http://example.com/goku.png",
            raca_id=raca.id
        )

        goku_saga = create_object(
            PersonagemSaga,
            poderMult=20,
            imagem="http://example.com/goku_saga.png",
            persBase_id=goku_base.id,
            saga_id=saga.id
        )

        assert goku_saga.persBase.nome == "Goku"
        assert goku_saga.saga.desc.startswith("Saga")


def test_many_to_many_transformacoes():
    with app.app_context():
        goku_saga = get_object_by_attribute(PersonagemSaga, "poderMult", 20)

        ssj = create_object(
            Transformacao,
            nome="Super Saiyajin",
            cor="Dourado",
            especial="Aumenta poder",
            efeitoCol="Cabelo em pé",
            poderMult=50,
            imagem="http://example.com/ssj.png",
            limMinutos=30
        )

        goku_saga.transformacoes.append(ssj)
        db.session.commit()

        # Check the relationship
        assert ssj in goku_saga.transformacoes
        assert goku_saga in ssj.personagens


def test_delete_raca_cascades():
    """Check cascade deletion behavior"""
    with app.app_context():
        raca = get_object_by_attribute(Raca, "nome", "Humano")
        delete_object(raca)

        remaining = db.session.query(Raca).filter_by(nome="Humano").first()
        assert remaining is None

def dump_all(model_class):
    objs = get_objects(model_class)
    return [
        {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        for obj in objs
    ]

def test_dump_all_data():
    with app.app_context():
        import json
        for i in [Obra, Saga, Raca, Transformacao, PersonagemBase, PersonagemSaga]:
            data = dump_all(i)
            print(str(i))
            print(json.dumps(data, indent=4, ensure_ascii=False, default=str))

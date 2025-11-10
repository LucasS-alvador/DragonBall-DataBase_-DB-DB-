# import pytest
# from datetime import date

# from config import app
# from service.common_service import create_object, get_object_by_attribute, delete_object
# import warnings
# from model.personagembase import * 
# from model.personagemsaga import *
# from model.saga import *

# def test_create_personagem_saga():
#     with app.app_context():
#         personagem_saga = create_object(
#             PersonagemSaga,
#             poderMult=20,
#             imagem="http://example.com/personagem.png",
#             persBase_id=0,
#             saga_id=0
#         )
#         assert personagem_saga.id is not None
#         assert isinstance(personagem_saga.id, int)
#         assert personagem_saga.imagem == "http://example.com/personagem.png"

# def test_get_personagem_saga():
#     with app.app_context():
#         personagem_saga = get_object_by_attribute(PersonagemSaga, "nome", "Personagem de Teste")
#         assert personagem_saga is not None
#         assert personagem_saga.nome == "Personagem de Teste"
#         assert personagem_saga.dtNasc == date(1990, 1, 1)

# def test_delete_personagem_saga():
#     with app.app_context():
#         personagem_saga = get_object_by_attribute(PersonagemSaga, "nome", "Personagem de Teste")
#         assert personagem_saga is not None
        
#         result = delete_object(personagem_saga)
#         assert result is True

#         # Confirm deletion
#         personagem_saga = get_object_by_attribute(PersonagemSaga, "nome", "Personagem de Teste")
#         assert personagem_saga is None

# def test_create_personagem_base():
#     with app.app_context():
#         personagem_base = create_object(
#             PersonagemBase,
#             nome="Personagem Base de Teste",
#             descricao="Descrição do Personagem Base de Teste",
#             dtNasc=date(1985, 5, 15),
#             dtMorte=None,
#             imagem="http://example.com/personagembase.png"
#         )
#         assert personagem_base.id is not None
#         assert isinstance(personagem_base.id, int)
#         assert personagem_base.nome == "Personagem Base de Teste"
#         assert personagem_base.imagem == "http://example.com/personagembase.png"
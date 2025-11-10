# import pytest
# from datetime import date

# from config import app
# from service.common_service import create_object, get_object_by_attribute, delete_object
# # import warnings
# from model.obra import *
# from model.saga import *
# from model.raca import *
# from model.personagembase import *
# from model.personagemsaga import *
# from model.transformacao import *

# def test_create_raca():
#     with app.app_context():
#         raca = create_object(
#             Raca,
#             nome='Humano',
#             cor='Pele clara',
#             desc='Descrição da raça humana',
#             poderBase=10,
#             imagem='http://example.com/raca.png'
#         )
#         assert raca.id is not None
#         assert isinstance(raca.id, int)
#         assert raca.nome == "Humano"
#         assert raca.desc == "Descrição da raça humana"

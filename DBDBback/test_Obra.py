# import pytest
# from datetime import date

# from config import app
# from service.common_service import create_object, get_object_by_attribute, delete_object
# from model.obra import Obra  # Adjust path to where your Obra model is
# from model.saga import Saga
# import warnings

# def test_create_obra():
#     with app.app_context():
#         obra = create_object(
#             Obra,
#             nome="Obra de Teste",
#             dtIni=date(2022, 1, 1),
#             dtFim=date(2022, 12, 31),
#             imagem="http://example.com/img.png"
#         )
#         assert obra.id is not None
#         assert isinstance(obra.id, int)
#         assert obra.nome == "Obra de Teste"
#         assert obra.imagem == "http://example.com/img.png"

# def test_get_obra():
#     with app.app_context():
#         obra = get_object_by_attribute(Obra, "nome", "Obra de Teste")
#         assert obra is not None
#         assert obra.nome == "Obra de Teste"
#         assert obra.dtIni == date(2022, 1, 1)

# def test_delete_obra():
#     with app.app_context():
#         obra = get_object_by_attribute(Obra, "nome", "Obra de Teste")
#         assert obra is not None
        
#         result = delete_object(obra)
#         assert result is True

#         # Confirm deletion
#         obra = get_object_by_attribute(Obra, "nome", "Obra de Teste")
#         assert obra is None

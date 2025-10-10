# import pytest
# from src.config import app
# from src.service.common_service import create_object, get_object_by_attribute, delete_object
# from src.model.obra import Obra
# from src.model.saga import Saga
# from datetime import date
# from warnings import warn

# def test_create_saga():
#     with app.app_context():
#         # Create the parent Obra
#         obra = create_object(
#             Obra,
#             nome="Obra com Saga",
#             dtIni=date(2023, 1, 1),
#             dtFim=date(2023, 12, 31),
#             imagem="http://example.com/saga.png"
#         )

#         # Create the Saga linked to Obra
#         saga = create_object(
#             Saga,
#             desc="Saga Teste",
#             epIni=1,
#             epFim=12,
#             obra_id=obra.id
#         )

#         assert saga.id is not None
#         assert saga.desc == "Saga Teste"
#         assert saga.epFim == 12
#         assert saga.obra_id == obra.id

# def test_get_saga():
#     with app.app_context():
#         saga = get_object_by_attribute(Saga, "desc", "Saga Teste")
#         assert saga is not None
#         assert saga.desc == "Saga Teste"
#         assert saga.obra is not None
#         assert saga.obra.nome == "Obra com Saga"

# def test_delete_saga():
#     with app.app_context():
#         saga = get_object_by_attribute(Saga, "desc", "Saga Teste")
#         assert saga is not None
#         ok = delete_object(saga)
#         assert ok is True

#         # Confirm it's gone
#         saga = get_object_by_attribute(Saga, "desc", "Saga Teste")
        
#         assert saga is None
        

# def test_cascade_delete_with_obra():
#     with app.app_context():
#         # Recreate Obra + Saga
#         obra = create_object(
#             Obra,
#             nome="Cascade Obra",
#             dtIni=date(2022, 1, 1),
#             dtFim=date(2022, 6, 1),
#             imagem=""
#         )

#         saga = create_object(
#             Saga,
#             desc="Cascade Saga",
#             epIni=5,
#             epFim=10,
#             obra_id=obra.id
#         )

#         # Delete Obra (should cascade to Saga)
#         delete_object(obra)
        
#         # Saga should be gone
#         deleted_saga = get_object_by_attribute(Saga, "desc", "Cascade Saga")
#         assert deleted_saga is None

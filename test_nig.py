import pytest

from src.config import *
from src.service.common_service import *
from src.model.obra import Obra
from src.model.saga import Saga

def test_creation():
    with app.app_context():
        obra = create_object(Obra, nome="Dragon Ball Z", dtIni=date(1990, 1, 1), dtFim=date(1999, 2, 2))
        assert obra.id is not None
        assert isinstance(obra.id, int)
        assert obra.nome == "Dragon Ball Z"

        print(get_objects(Obra))

        
        # obj = create_object(Saga, 
        #     model="Toyota Corolla", 
        #     year=2020,
        #     person_id=person.id)
        # assert obj.id is not None
        # assert isinstance(obj.id, int)
        # assert obj.model == "Toyota Corolla"         

# def test_obj_delete():
#     with app.app_context():
#         obj = get_object_by_attribute(Car, "model", "Toyota Corolla")   
#         assert obj.model == "Toyota Corolla"
#         ok = delete_object(obj)
#         assert ok == True

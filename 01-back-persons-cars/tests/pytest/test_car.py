import pytest

from src.config import *
from src.service.common_service import *
from src.model.person import Person
from src.model.car import Car

def test_creation():
    with app.app_context():
        person = create_object(Person, 
            name="Mary Jane", 
            email="maja@gmail.com")
        
        obj = create_object(Car, 
            model="Toyota Corolla", 
            year=2020,
            person_id=person.id)
        assert obj.id is not None
        assert isinstance(obj.id, int)
        assert obj.model == "Toyota Corolla"         

def test_obj_delete():
    with app.app_context():
        obj = get_object_by_attribute(Car, "model", "Toyota Corolla")   
        assert obj.model == "Toyota Corolla"
        ok = delete_object(obj)
        assert ok == True



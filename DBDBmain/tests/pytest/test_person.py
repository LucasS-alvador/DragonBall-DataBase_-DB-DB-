# import pytest

# from src.config import *
# from src.service.common_service import *
# from src.model.person import Person

# def test_creation():
#     with app.app_context():
#         obj = create_object(Person, 
#             name="Jack Johnson", 
#             email="jack@gmail.com")
        
#         assert obj.id is not None
#         assert isinstance(obj.id, int)
#         assert obj.name == "Jack Johnson"

# def test_obj_delete():
#     with app.app_context():
#         obj = get_object_by_attribute(Person, "name", "Jack Johnson")   
#         assert obj.name == "Jack Johnson"
#         ok = delete_object(obj)
#         assert ok == True
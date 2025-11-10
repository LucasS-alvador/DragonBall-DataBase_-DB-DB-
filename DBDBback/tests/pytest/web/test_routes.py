# from config import app, db
# from datetime import date, time
# from route.routes import *

# import pytest

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()
#         yield client

# def test_person_crud(client):

#     # POST
#     res = client.post('/persons', 
#                       json={"name": "Alice Smith", "email": "alice@gmail.com"})
#     assert res.status_code == 201
#     person_id = res.get_json()["details"]["id"]
#     print(f"Created person with ID: {person_id}")

#     # GET LIST
#     res = client.get('/persons')
#     assert res.status_code == 200
#     json = res.get_json()
#     assert json["result"] == "ok"
#     assert isinstance(json["details"], list)
#     print(f"Persons found: {len(json['details'])}")

#     # DELETE
#     res = client.delete(f"/persons/{person_id}")
#     assert res.status_code == 204
#     print(f"Person with ID {person_id} deleted successfully.")
    
# def test_car_crud(client):

#     # POST
#     res = client.post('/cars',
#                     json={"model": "Honda Civic", "year": 2021, "person_id": 1})    
#     assert res.status_code == 201
#     car_id = res.get_json()["details"]["id"]
#     print(f"Created car with ID: {car_id}")

#     # GET LIST
#     res = client.get('/cars')
#     assert res.status_code == 200
#     json = res.get_json()
#     assert json["result"] == "ok"
#     assert isinstance(json["details"], list)
#     print(f"Cars found: {len(json['details'])}")

#     # DELETE
#     res = client.delete(f"/cars/{car_id}")
#     assert res.status_code == 204
#     print(f"Car with ID {car_id} deleted successfully.")
from src.config import *
from src.service.common_service import *
from src.model.obra import *
from src.model.saga import *
from src.model.raca import *
from src.model.transformacao import *
from src.model.personagembase import *
from src.model.personagemsaga import *
from src.utils import *
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Obra: (Nome, data_ini, data_fin, imagem)
# Saga: (Nome, desc, ep_ini, ep_fin, Obra_id, imagem)

# Raça: (Nome, cor, desc, poderBase, imagem)
# Transformação: (Nome, cor, poder, especial, efeitoCol, imagem, tempo_lim)
# PersonagemBase: (Nome, Raça_id, data_nasc, sexo,  imagem)
# PersonagemSaga: (PersonagemBase_id, Saga_id, poder, Trans_id[], imagem)


# default route
@app.route('/')
def index():
    return "Welcome to the API. Use endpoints."

# ---------------------------------------------------------------- POST's (creation) ----------------------------------------------------------------

# generic object creation: auxiliar function
def create_simple_object(mclass, data):
    try:
        myjson = {"result": "ok"}               # prepare some default answer
        user = create_object(mclass, **data)    # try to create the object
        response = serialize_model(user)        # prepare an answer with the serialized object
        myjson.update({"details": response})    # add the serialized object to the answer
        return myjson                           # return the answer
    except Exception as ex:
        print(f"Error during object creation: {ex}")
        return {"result":"error", "details":f"error during object creation: {ex}"}
    
# @app.route('/persons', methods=['POST'])
# def create_person():
#     data = request.json                         # get the data
#     answer = create_simple_object(Person, data) # try to create the object
#     return jsonify(answer), 201 if answer["result"] == "ok" else 500 # return created or internal error

# @app.route('/cars', methods=['POST'])
# def create_cars():
#     data = request.json                        # get the data
#     answer = create_simple_object(Car, data)   # try to create the object
#     return jsonify(answer), 201 if answer["result"] == "ok" else 500 # return created or internal error

@app.route('/obra', methods=['POST'])
def create_obra():
    data = request.json
    answer = create_simple_object(Obra, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/saga', methods=['POST'])
def create_saga():
    data = request.json
    answer = create_simple_object(Saga, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/raca', methods=['POST'])
def create_raca():
    data = request.json
    answer = create_simple_object(Raca, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/transformacao', methods=['POST'])
def create_transformacao():
    data = request.json
    answer = create_simple_object(Transformacao, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/personagembase', methods=['POST'])
def create_personagembase():
    data = request.json
    answer = create_simple_object(PersonagemBase, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/personagemsaga', methods=['POST'])
def create_personagemsaga():
    data = request.json
    answer = create_simple_object(PersonagemSaga, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

# @app.route('/example', methods=['POST'])
# def create_example():
#     data = request.json
#     answer = create_simple_object(Example, data)
#     return jsonify(answer), 201 if answer["result"] == "ok" else 500

# ---------------------------------------------------------------- GET's LIST ----------------------------------------------------------------

# auxiliar function
def get_objects_helper(mclass):
    try:
        myjson = {"result": "ok"}   
        objs = get_objects(mclass)                   # get all objects
        response = [serialize_model(u) for u in objs]  # serialize the objects
        myjson.update({"details": response})            # add the serialized object to the answer
        return myjson
    except Exception as ex:
        print(f"Error during {mclass} listing: {ex}")
        return {"result": "error", "details": f"error during {mclass} listing: {ex}"}

# @app.route('/persons', methods=['GET'])
# def list_persons():
#     myjson = get_objects_helper(Person)
#     return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

# @app.route('/cars', methods=['GET'])
# def list_cars():
#     myjson = get_objects_helper(Car)
#     return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

@app.route('/obra', methods=['GET'])
def list_obra():
    myjson = get_objects_helper(Obra)
    return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

@app.route('/saga', methods=['GET'])
def list_saga():
    myjson = get_objects_helper(Saga)
    return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

@app.route('/raca', methods=['GET'])
def list_raca():
    myjson = get_objects_helper(Raca)
    return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

@app.route('/transformacao', methods=['GET'])
def list_transformacao():
    myjson = get_objects_helper(Transformacao)
    return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

@app.route('/personagembase', methods=['GET'])
def list_personagembase():
    myjson = get_objects_helper(PersonagemBase)
    return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

@app.route('/personagemsaga', methods=['GET'])
def list_personagemsaga():
    myjson = get_objects_helper(PersonagemSaga)
    return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

# @app.route('/example', methods=['GET'])
# def list_example():
#     myjson = get_objects_helper(Anus)
#     return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500

# ---------------------------------------------------------------- DELETE's ----------------------------------------------------------------

def delete_object(mclass, obj_id):
    try:
        myjson = {"result": "ok"}  # prepare a "good" default answer :-)   
    
        obj = get_object_by_attribute(mclass, "id", obj_id)
        if not obj:
            return {"result": "error", "details": f"{mclass}({obj_id}) not found "}
        db.session.delete(obj)
        db.session.commit()
        myjson.update({"details": "ok"})
        return myjson
    except Exception as ex:
        print(f"Error during hard delete of object {mclass} with id {obj_id}: {ex}")
        return {"result": "error", "details": f"error during object ({mclass}) exclusion: {ex}"}

# @app.route('/persons/<int:obj_id>', methods=['DELETE'])
# def delete_person(obj_id):
#     myjson = delete_object(Person, obj_id)
#     return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

# @app.route('/cars/<int:obj_id>', methods=['DELETE'])
# def delete_car(obj_id):
#     myjson = delete_object(Car, obj_id)
#     return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

@app.route('/obra/<int:obj_id>', methods=['DELETE'])
def delete_obra(obj_id):
    myjson = delete_object(Obra, obj_id)
    return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

@app.route('/saga/<int:obj_id>', methods=['DELETE'])
def delete_saga(obj_id):
    myjson = delete_object(Saga, obj_id)
    return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

@app.route('/raca/<int:obj_id>', methods=['DELETE'])
def delete_raca(obj_id):
    myjson = delete_object(Raca, obj_id)
    return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

@app.route('/transformacao/<int:obj_id>', methods=['DELETE'])
def delete_transformacao(obj_id):
    myjson = delete_object(Transformacao, obj_id)
    return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

@app.route('/personagembase/<int:obj_id>', methods=['DELETE'])
def delete_personagembase(obj_id):
    myjson = delete_object(PersonagemBase, obj_id)
    return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

@app.route('/personagemsaga/<int:obj_id>', methods=['DELETE'])
def delete_personagemsaga(obj_id):
    myjson = delete_object(PersonagemSaga, obj_id)
    return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

# @app.route('/example/<int:obj_id>', methods=['DELETE'])
# def delete_example(obj_id):
#     myjson = delete_object(Example, obj_id)
#     return jsonify(myjson), 204 if myjson['result'] == 'ok' else 500

# ---------------------------------------------------------------- END ----------------------------------------------------------------
print("Routes loaded successfully. (reached routes.py)")

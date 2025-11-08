from src.app import app
from src.database import db
from src.service.common_service import *
from src.model.obra import *
from src.model.saga import *
from src.model.raca import *
from src.model.transformacao import *
from src.model.personagembase import *
from src.model.personagemsaga import *
from src.utils import *
from flask import render_template, request, redirect, url_for, jsonify

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
    try:
        data = request.json
        print("[API] POST /obra - Dados recebidos:", data)
        
        # Validação básica dos campos
        required_fields = ['nome', 'dtIni', 'dtFim']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "result": "error",
                    "details": f"Campo obrigatório ausente: {field}"
                }), 400
        
        # Tenta criar a obra
        obra = create_object(Obra, **data)
        response = {
            "result": "ok",
            "details": {
                "id": obra.id,
                "nome": obra.nome,
                "dtIni": obra.dtIni.isoformat() if obra.dtIni else None,
                "dtFim": obra.dtFim.isoformat() if obra.dtFim else None,
                "imagem": obra.imagem
            }
        }
        print("[API] POST /obra - Obra criada com sucesso:", response)
        return jsonify(response), 201
        
    except ValueError as e:
        print("[API] POST /obra - Erro de validação:", str(e))
        return jsonify({
            "result": "error",
            "details": str(e)
        }), 400
    except Exception as e:
        import traceback
        print("[API] POST /obra - Erro interno:", str(e))
        print(traceback.format_exc())
        return jsonify({
            "result": "error",
            "details": f"Erro ao criar obra: {str(e)}"
        }), 500

@app.route('/saga', methods=['POST'])
def create_saga():
    try:
        data = request.json
        print("[API] POST /saga - Dados recebidos:", data)

        # Validação dos dados
        required_fields = ['desc', 'epIni', 'epFim', 'obra_id']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "result": "error",
                    "details": f"Campo obrigatório ausente: {field}"
                }), 400

        # Validação da obra_id
        obra = get_object_by_attribute(Obra, 'id', data['obra_id'])
        if not obra:
            return jsonify({
                "result": "error",
                "details": f"Obra com ID {data['obra_id']} não encontrada"
            }), 400

        # Cria a saga
        saga = create_object(Saga, **data)
        response = {
            "result": "ok",
            "details": serialize_model(saga)
        }
        print("[API] POST /saga - Saga criada com sucesso:", response)
        return jsonify(response), 201

    except ValueError as e:
        print("[API] POST /saga - Erro de validação:", str(e))
        return jsonify({
            "result": "error",
            "details": str(e)
        }), 400

    except Exception as e:
        import traceback
        print("[API] POST /saga - Erro interno:", str(e))
        print(traceback.format_exc())
        return jsonify({
            "result": "error",
            "details": f"Erro ao criar saga: {str(e)}"
        }), 500

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
    try:
        data = request.json
        personagem = create_object(PersonagemBase, **data)
        return jsonify({
            "result": "ok",
            "details": personagem.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({
            "result": "error",
            "details": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "result": "error",
            "details": f"Erro ao criar personagem: {str(e)}"
        }), 500

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
        if not objs:
            return {"result": "ok", "details": []}
        response = [serialize_model(u) for u in objs]  # serialize the objects
        myjson.update({"details": response})            # add the serialized object to the answer
        print(f"[API] GET {mclass.__name__} - Found {len(objs)} objects")
        return myjson
    except Exception as ex:
        import traceback
        print(f"Error during {mclass.__name__} listing: {ex}")
        print(traceback.format_exc())
        return {"result": "error", "details": f"error during {mclass.__name__} listing: {str(ex)}"}

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
    print("[API] GET /raca - Listando raças")
    try:
        myjson = get_objects_helper(Raca)
        print("[API] GET /raca - Resposta:", myjson)
        return jsonify(myjson), 200 if myjson['result'] == 'ok' else 500
    except Exception as e:
        print("[API] GET /raca - Erro:", str(e))
        return jsonify({"result": "error", "details": "Erro interno ao listar raças"}), 500

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




@app.route('/api/<string:model>', methods=['GET'])
def get_all(model):
    models = {
        "obra": Obra,
        "saga": Saga,
        "raca": Raca,
        "personagembase": PersonagemBase,
        "personagemsaga": PersonagemSaga,
        "transformacao": Transformacao
    }
    Model = models.get(model.lower())
    if not Model:
        return jsonify({"error": "Model not found"}), 404

    objs = db.session.query(Model).all()
    return jsonify([
        {c.name: (getattr(o, c.name).isoformat() if hasattr(getattr(o, c.name), "isoformat") else getattr(o, c.name))
         for c in o.__table__.columns}
        for o in objs
    ])

@app.route('/api/<string:model>/<int:id>', methods=['GET'])
def get_by_id(model, id):
    models = {
        "obra": Obra,
        "saga": Saga,
        "raca": Raca,
        "personagembase": PersonagemBase,
        "personagemsaga": PersonagemSaga,
        "transformacao": Transformacao
    }
    Model = models.get(model.lower())
    if not Model:
        return jsonify({"error": "Model not found"}), 404

    o = db.session.get(Model, id)
    if not o:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        c.name: (getattr(o, c.name).isoformat() if hasattr(getattr(o, c.name), "isoformat") else getattr(o, c.name))
        for c in o.__table__.columns
    })





@app.route("/api/obras", methods=["GET"])
def get_obras():
    return jsonify([obra.to_dict() for obra in Obra.query.all()])

@app.route("/api/obras/<int:id>", methods=["GET"])
def get_obra(id):
    obra = Obra.query.get_or_404(id)
    return jsonify(obra.to_dict())

@app.route("/api/obras", methods=["POST"])
def add_obra():
    data = request.json
    nova = Obra(**data)
    db.session.add(nova)
    db.session.commit()
    return jsonify(nova.to_dict()), 201






# ---------------------------------------------------------------- END ----------------------------------------------------------------
print("Routes loaded successfully. (reached routes.py)")

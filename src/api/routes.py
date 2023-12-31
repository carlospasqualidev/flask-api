
from flask import Blueprint, jsonify,request
from src.api.services.user.findUserByIdService import findUserByIdService

from src.api.controllers.music.findManyMusicsController import findManyMusicsController
from src.api.controllers.auth.loginController import loginController
from src.api.services.error.handleError import addError, getErrors
from src.api.controllers.user.createUserController import createUserController
from src.api.controllers.user.updateUserController import updateUserController
from src.api.controllers.user.deleteUserController import deleteUserController
from src.api.controllers.machineLearning.predictMusicPopularityController import predictMusicPopularityController

routerBlueprint = Blueprint('api', __name__)

# region PREDICT MODEL
@routerBlueprint.route("/predicts", methods=["POST"])
async def predict():
    data = request.get_json()

    #region VALIDATE FIELDS
    if(data["dance"] == ''):
         addError("Campo dance é obrigatório.")
    if(data["energy"] == ''):
        addError("Campo energy é obrigatório.")
    if(data["key"] == ''):
        addError("Campo key é obrigatório.")
    if(data["speech"] == ''):
        addError("Campo speech é obrigatório.")
    if(data["acoustic"] == ''):
        addError("Campo acoustic é obrigatório.")
    if(data["instrumental"] == ''):
        addError("Campo instrumental é obrigatório.")
    if(data["time"] == ''):
        addError("Campo time é obrigatório.")
    if(data["name"] == ''):
        addError("Campo name é obrigatório.")
    if(data["userId"] == ''):
        addError("Campo userId é obrigatório.")
    
    user = await findUserByIdService(data["userId"])
    if (user is None):
        return addError("Usuário não encontrado na base de dados.") 

    #region HANDLE ERRORS  
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),422
    #endregion

    #endregion

    music = await predictMusicPopularityController(data["dance"],
                                           data["energy"],
                                           data["key"],
                                           data["speech"],
                                           data["acoustic"],
                                           data["instrumental"],
                                           data["time"],
                                           data["name"],
                                           data["userId"])

    return jsonify({"message": ["Modelo de predição executado com sucesso."], "music": music}),201

@routerBlueprint.route("/predicts/<userId>", methods=["GET"])
async def musics(userId):
   
    musics = await findManyMusicsController(userId)

    #region HANDLE ERRORS  
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),404
    #endregion

    return jsonify({"musics":musics} ),200

# endregion

# region USER
@routerBlueprint.route("/users", methods=["POST"])
async def create():
    data = request.get_json()
   
    user = await createUserController(data['email'], data['password'] )

    #region HANDLE ERRORS  
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),422
    #endregion

    return jsonify({"message": ["Usuario cadastrado com sucesso."],"user":user} ),201

@routerBlueprint.route("/users", methods=["PUT"])
async def update():
    data = request.get_json()
   
    user = await updateUserController(data['id'] ,data['email'], data['password'] )

    #region HANDLE ERRORS  
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),422
    #endregion

    return jsonify({"message":["Usuario atualizado com sucesso."],"user":user} ),200


@routerBlueprint.route("/users/<id>", methods=["DELETE"])
async def delete(id):
   
    await deleteUserController(id)

    #region HANDLE ERRORS  
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),404
    #endregion

    return jsonify({"message":["Usuario excluído com sucesso."]} ),200

# endregion

# region LOGIN
@routerBlueprint.route("/login", methods=["POST"])
async def login():
    data = request.get_json()
    
    user = await loginController(data['email'], data['password'])

    #region HANDLE ERRORS  
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),404
    #endregion

    return jsonify({"user":user} ),200
# endregion
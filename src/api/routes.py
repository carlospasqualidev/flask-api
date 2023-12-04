
from flask import Blueprint, jsonify,request
from src.api.controllers.auth.loginController import loginController
from src.api.services.error.handleError import getErrors
from src.api.controllers.user.createUserController import createUserController


routerBlueprint = Blueprint('api', __name__)

@routerBlueprint.route("/users", methods=["POST"])
async def create():
    data = request.get_json()
   
    user = await createUserController(data['email'], data['password'] )

    #=============== HANDLE ERRORS =============== 
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),422
    #============================================= 

    return jsonify({"message": "Usuario cadastrado com sucesso.","user":user} ),201

   
@routerBlueprint.route("/login", methods=["POST"])
async def login():
    data = request.get_json()
    
    user = await loginController(data['email'], data['password'])

    #=============== HANDLE ERRORS =============== 
    errors = getErrors()
    if(errors):
        return jsonify({"message": errors,} ),422
    #============================================= 

    return jsonify({"user":user} ),200
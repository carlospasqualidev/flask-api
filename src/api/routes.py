
from flask import Blueprint, jsonify,request
from src.api.controllers.createUserController import createUserController
from src.api.controllers.loginController import loginController

routerBlueprint = Blueprint('api', __name__)

@routerBlueprint.route("/users", methods=["POST"])
async def create():
    data = request.get_json()
   
    user = await createUserController(data['email'], data['password'] )

    return jsonify({"message": "Usuario cadastrado com sucesso.","user":user} ),201

   
@routerBlueprint.route("/login", methods=["POST"])
async def login():
    data = request.get_json()
   
    user = await loginController(data['email'], data['password'])

    return jsonify({"user":user} ),200
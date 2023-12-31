from flask import Flask
from flask_cors import CORS
from src.api.routes import routerBlueprint


# INIT FLASK
app = Flask(__name__)

# REGISTER ROUTER BLUEPRINT
app.register_blueprint(routerBlueprint, url_prefix='/api')

cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


if __name__ == '__main__':
    app.run(debug=True)

#RUN THIS PROJECT

# python3 -m venv .venv 
# .venv\Scripts\activate (WINDOWS)  ||  source .venv/bin/activate (LINUX)
# flask --app server --debug run 
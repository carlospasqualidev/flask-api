from flask import Flask
from src.api.routes import routerBlueprint

# INIT FLASK
app = Flask(__name__)

# REGISTER ROUTER BLUEPRINT
app.register_blueprint(routerBlueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)


#RUN THIS PROJECT

# .venv\Scripts\activate
# flask --app server --debug run 
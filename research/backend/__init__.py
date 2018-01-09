from flask import Flask
from flask import request
from flask import Blueprint
from flask_restful import Api

from restful.register import Register
from restful.login import Login


app = Flask(__name__)

bp_api = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp_api)

api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

app.register_blueprint(bp_api)

if __name__ == "__main__":
    app.run(debug = True)

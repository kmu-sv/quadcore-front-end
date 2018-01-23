from flask import Flask
from flask import request
from flask import Blueprint
from flask_restful import Api

app = Flask(__name__)

bp_api = Blueprint("api", __name__)
api = Api(bp_api)

from quadcore.restful.github.login import GithubLogin
from quadcore.restful.github.auth import GithubAuth
from quadcore.restful.github.logout import GithubLogout
from quadcore.restful.profile import Profile

api.add_resource(GithubLogin, "/login/github")
api.add_resource(GithubAuth, "/login/github/authorized")
api.add_resource(GithubLogout, "/logout")
api.add_resource(Profile, "/profile")

app.register_blueprint(bp_api)


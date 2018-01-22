from flask import Flask
from flask import request
from flask import Blueprint
from flask_restful import Api
from flask_oauthlib.client import OAuth

app = Flask(__name__)
oauth = OAuth(app) 

bp_api = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp_api)

from quadcore.restful.register import Register
from quadcore.restful.github.login_github import LoginGithub
from quadcore.restful.github.auth_github import AuthGithub
from quadcore.restful.github.logout_github import LogoutGithub

api.add_resource(Register, "/register")
api.add_resource(LoginGithub, "/login/github")
api.add_resource(AuthGithub, "/login/github/authorized")
api.add_resource(LogoutGithub, "/logout")

app.register_blueprint(bp_api)


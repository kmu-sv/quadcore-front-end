from flask import Flask
from flask import request
from flask import Blueprint
from flask_restful import Api

app = Flask(__name__)

bp_api = Blueprint("api", __name__)
api = Api(bp_api)

from quadcore.restful.github.login import GithubLogin
from quadcore.restful.github.auth import GithubAuth
from quadcore.restful.linkedin.login import LinkedInLogin
from quadcore.restful.linkedin.auth import LinkedInAuth
from quadcore.restful.logout import Logout
from quadcore.restful.profile import Profile
from quadcore.restful.username import Username
from quadcore.restful.feed import Feed

api.add_resource(GithubLogin, "/login/github")
api.add_resource(GithubAuth, "/login/github/authorized")
api.add_resource(LinkedInLogin, "/login/linkedin")
api.add_resource(LinkedInAuth, "/login/linkedin/authorized")
api.add_resource(Logout, "/logout")
api.add_resource(Profile, "/user/profile")
api.add_resource(Username, "/user/username")
api.add_resource(Feed, "/feed")

app.register_blueprint(bp_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
from flask import Flask
from flask import request
from flask import Blueprint
from flask_restful import Api
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

bp_api = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp_api)

from quadcore.restful.github.login import GithubLogin
from quadcore.restful.github.auth import GithubAuth
from quadcore.restful.linkedin.login import LinkedInLogin
from quadcore.restful.linkedin.auth import LinkedInAuth
from quadcore.restful.user.logout import Logout
from quadcore.restful.user.profile import Profile
from quadcore.restful.user.profile.new import ProfileNew
from quadcore.restful.user.profile.update import ProfileUpdate
from quadcore.restful.user.metadata import Metadata
from quadcore.restful.feed import Feed
from quadcore.restful.user.profile.check.auth import CheckAuth
from quadcore.restful.user.profile.check.username import CheckUsername

api.add_resource(GithubLogin, "/login/github")
api.add_resource(GithubAuth, "/login/github/authorized")
api.add_resource(LinkedInLogin, "/login/linkedin")
api.add_resource(LinkedInAuth, "/login/linkedin/authorized")
api.add_resource(Logout, "/logout")
api.add_resource(Profile, "/user/profile")
api.add_resource(ProfileNew, "/user/profile/new")
api.add_resource(ProfileUpdate, "/user/profile/update")
api.add_resource(Metadata, "/user/metadata")
api.add_resource(Feed, "/feed")
api.add_resource(CheckAuth, "/check/auth")
api.add_resource(CheckUsername, "/check/username")

app.register_blueprint(bp_api)

if __name__ == "__main__":
    app.run(debug=True)

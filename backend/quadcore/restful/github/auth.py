from flask import Flask, redirect, session, request
from flask_restful import Resource
from quadcore.config import Config
from quadcore.manager.platform.github import Github
from quadcore.manager.data import DataManager

class GithubAuth(Resource):
    def get(self):
        access_token = Github.access_token(request.args["code"], request.args["state"])
        auth_info = Github.get_auth_info(access_token)
        if auth_info != None:
            session["email"] = auth_info["email"]
            session["github_token"] = access_token
            username = DataManager.check_email_username(auth_info["email"])
            if username != None:
                session["username"] = username
                return redirect(Config.oauth_success_url)
            else:
                print("in auth")
                print(session["github_token"])
                return redirect(Config.oauth_signup_url)
        else:
            return redirect(Config.oauth_failure_url)
        
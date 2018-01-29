from flask import Flask, redirect, session, request
from flask_restful import Resource
from quadcore.config import Config
from quadcore.manager.platform.linkedin import LinkedIn
from quadcore.manager.data import DataManager

class LinkedInAuth(Resource):
    def get(self):
        access_token = LinkedIn.access_token(request.args["code"])
        auth_info = LinkedIn.get_auth_info(access_token)

        if auth_info != None:
            session["username"] = auth_info["username"]
            session["email"] = auth_info["email"]
            session["linkedin_token"] = access_token

            if DataManager.is_exist_user(auth_info["email"]):
                return redirect(Config.oauth_success_url)
            else:
                return redirect(Config.oauth_signup_url)
        else:
            return redirect(Config.oauth_failure_url)
        
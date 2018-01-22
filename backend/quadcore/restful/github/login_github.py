from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api
from quadcore.manager.auth import AuthManager as am
from quadcore import app, oauth

class LoginGithub(Resource):

    def get(self):
        return am.oauth_github.authorize(callback="http://api.quadcore.news/login/github/authorized", _external=True)
        # return {
        #     "result": 1,
        #     "reason": "You approached wrong way!"
        # }

    def post(self):
        return am.oauth_github.authorize(callback="http://api.quadcore.news/login/github/authorized", _external=True)
    
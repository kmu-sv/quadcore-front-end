from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api
from quadcore.manager.auth import AuthManager as am

class LogoutGithub(Resource):

    def get(self):
        return {
            "result": 1,
            "reason": "You approached wrong way!"
        }

    def post(self):
        session.pop('github_token', None)
        return 'OK'

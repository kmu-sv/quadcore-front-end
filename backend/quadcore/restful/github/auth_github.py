from flask import Flask, redirect, url_for, session, request, jsonify, abort
from flask_restful import Resource, Api
from quadcore.manager.auth import AuthManager as am

class AuthGithub(Resource):

    def get(self):
        return {
            "result": 1,
            "reason": "You approached wrong way!"
        }

    def post(self):
        resp = am.oauth_github.authorized_response()
        if resp is None:
            abort(401, message='Access denied!')
        user = am.oauth_github.get('user')
        user.data['access_token'] = session['github_token'][0]
        return jsonify(user.data)
    
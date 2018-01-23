from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api
from quadcore.manager.auth.github import GithubAuthManager as gm
from quadcore.config import Config

class GithubLogin(Resource):
    def get(self):
        return redirect(gm.identify_url_generate(
            Config.github_redirect_url,
            Config.github_scope
        ))

    def post(self):
        return {
            "result": 1,
            "cause": "You approached wrong way!"
        }
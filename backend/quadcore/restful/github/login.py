from flask import Flask, redirect
from flask_restful import Resource
from quadcore.manager.platform.github import Github

class GithubLogin(Resource):
    def get(self):
        return redirect(Github.auth_url())

    def post(self):
        return {
            "result": 1,
            "cause": "You approached wrong way!"
        }
from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api

class GithubLogout(Resource):
    def get(self):
        session.pop('github_token', None)
        return redirect("http://quadcore.news")

    def post(self):
        session.pop('github_token', None)
        return redirect("http://quadcore.news")

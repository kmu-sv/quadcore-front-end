from flask import Flask, redirect, session
from flask_restful import Resource, Api

class Logout(Resource):
    def get(self):
        session.pop('linkedin_token', None)
        session.pop('github_token', None)
        return redirect("http://quadcore.news")

    def post(self):
        session.pop('linkedin_token', None)
        session.pop('github_token', None)
        return redirect("http://quadcore.news")

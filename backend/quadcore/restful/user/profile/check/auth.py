from flask import Flask, session, request
from flask_restful import Resource
from quadcore.manager.data import DataManager

class CheckAuth(Resource):
    def get(self):
        try:
            return {
                "result": 0,
                "github": "github_token" in session,
                "linkedin": "linkedin_token" in session
            }
        except:
            return {
                "result": 1,
                "cause": "Authentication token parse error."
            }
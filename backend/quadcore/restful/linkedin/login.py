from flask import Flask, redirect
from flask_restful import Resource, Api
from quadcore.manager.auth.linkedin import LinkedInAuthManager as lm

class LinkedInLogin(Resource):
    def get(self):
        return redirect(lm.identify_url_generate())

    def post(self):
        return {
            "result": 1,
            "cause": "You approached wrong way!"
        }

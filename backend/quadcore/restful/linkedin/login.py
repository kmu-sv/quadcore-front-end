from flask import Flask, redirect
from flask_restful import Resource
from quadcore.manager.platform.linkedin import LinkedIn

class LinkedInLogin(Resource):
    def get(self):
        return redirect(LinkedIn.auth_url())

    def post(self):
        return {
            "result": 1,
            "cause": "You approached wrong way!"
        }

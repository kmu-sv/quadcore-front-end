from flask import Flask, session, request
from flask_restful import Resource
from quadcore.manager.data import DataManager

class CheckUsername(Resource):
    def get(self):
        args = json.loads(request.data.decode("utf-8"))
        username = args["username"]
        if DataManager.check_username(username):
            return {
                'result': 1
                'error': "Username already existed."
            }
        else:
            return {
                'result': 0
            }

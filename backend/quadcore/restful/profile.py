from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api

class Profile(Resource):
    # TODO(@harrydrippin): Provide more informations, Configure redis structure
    def get(self):
        if "username" in session:
            return {
                "result": 0,
                "username": session["username"]
            }
        else:
            return {
                "result": 1,
                "cause": "No credentials available"
            }

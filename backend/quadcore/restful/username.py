from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api

class Username(Resource):
    def get(self):
        if "github_token" in session or "linkedin_token" in session:
            return {
                "result": 0,
                "username": session["username"]
            }
        else:
            return {
                "result": 1,
                "cause": "Not logged yet"
            }
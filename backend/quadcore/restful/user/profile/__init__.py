from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api
from quadcore.manager.data import DataManager

class Profile(Resource):
    def get(self):
        if "github_token" in session or "linkedin_token" in session:
            result = DataManager.get_user_profile(session["email"])
            if result == None:
                return {
                    "result": 2,
                    "cause": "Not logged yet"
                }
            else:
                return {
                    "result": 0,
                    "info": result
                }

        else:
            return {
                "result": 1,
                "cause": "No credentials available"
            }

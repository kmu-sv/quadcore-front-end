from flask import Flask, session, request
from flask_restful import Resource
from quadcore.manager.data import DataManager

class ProfileUpdate(Resource):
    def get(self):
        args = json.loads(request.data.decode("utf-8"))
        if "github_token" in session or "linkedin_token" in session:
            result = DataManager.update_user_profile(args)
            if result == None:
                return {
                    "result": 2,
                    "cause": "Not sufficient data, or data has wrong form"
                }
            else:
                return {
                    "result": 0
                }

        else:
            return {
                "result": 1,
                "cause": "No credentials available"
            }

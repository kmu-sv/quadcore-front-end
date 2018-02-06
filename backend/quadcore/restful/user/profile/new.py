from flask import Flask, session, request
from flask_restful import Resource
import json
from quadcore.manager.data import DataManager

class ProfileNew(Resource):
    def post(self):
        args = json.loads(request.data.decode("utf-8"))
        if "github_token" in session or "linkedin_token" in session:
            if not DataManager.is_exist_user(session["email"]):
                result = DataManager.set_user_profile(args)
                if result == None:
                    return {
                        "result": 2,
                        "cause": "Not sufficient data, or data has wrong form"
                    }
                else:
                    map_info = DataManager.set_user_map(args)
                    return {
                        "result": 0
                    }
            else:
                return {
                    "result": 3,
                    "cause": "Exist email address"
                }

        else:
            return {
                "result": 1,
                "cause": "No credentials available"
            }

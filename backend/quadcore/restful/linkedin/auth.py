from flask import Flask, redirect, url_for, session, request, jsonify, abort
from flask_restful import Resource, Api
from quadcore.manager.auth.linkedin import LinkedInAuthManager as lm

class LinkedInAuth(Resource):
    def get(self):
        code = request.args["code"]
        access_token = lm.get_access_token(code)
        if access_token == None:
            return redirect("http://quadcore.news/")

        session["linkedin_token"] = access_token
        session["logged_in"] = True
        call_resp = lm.call("/v1/people/~?format=json", access_token)
        # TODO(@royeom) Set datas in redis
        session["username"] = call_resp["firstName"]
        # For demo
        return redirect("http://quadcore.news/feed.html")

from flask import Flask, redirect, url_for, session, request, jsonify, abort
from flask_restful import Resource, Api
from quadcore.manager.auth.github import GithubAuthManager as gm

class GithubAuth(Resource):
    def get(self):
        code, state = request.args["code"], request.args["state"]
        access_token = gm.get_access_token(code, state)
        if access_token == None:
            return redirect("http://quadcore.news/")

        session["github_token"] = access_token
        call_resp = gm.call("/user", access_token)
        # TODO(@harrydrippin) Set datas in redis
        session["username"] = call_resp["login"]
        return call_resp
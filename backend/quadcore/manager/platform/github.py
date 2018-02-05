from quadcore.config import Config
from quadcore.manager.platform import Platform
from urllib.parse import urlencode
from flask import session
import requests
import json

class Github(Platform):
    """
    Manage Github authentication process.
    """
    base_url = "https://api.github.com"
    authenticate_url = "https://github.com/login/oauth/authorize/?"
    redirect_url = "http://quadcore.news/api/login/github/authorized"
    access_token_url = "https://github.com/login/oauth/access_token"
    client_id = Config.github_consumer_key
    client_secret = Config.github_consumer_secret
    scope = ["read:user", "user:email", "repo:status", "read:org"]

    @classmethod
    def auth_url(cls, scope=scope, redirect=redirect_url):
        scope_string = str()
        for item in scope:
            scope_string += item + "%20"

        return cls.authenticate_url + urlencode({
            "client_id": cls.client_id,
            "redirect_uri": redirect,
            "scope": scope_string[:-3],
            "state": cls.state
        })

    @classmethod
    def access_token(cls, auth_code, state=str()):
        req_header = {
            "Accept": "application/json"
        }

        resp = requests.post(cls.access_token_url, data={
            "client_id": cls.client_id,
            "client_secret": cls.client_secret,
            "code": auth_code,
            "state": state
        }, headers=req_header).json()
        
        return (None if "error" in resp else resp["access_token"])

    @classmethod
    def call(cls, endpoint, token):
        req_header = {
            "Authorization": "token " + token
        }

        return requests.get(cls.base_url + endpoint, 
            headers=req_header).json()

    @classmethod
    def get_auth_info(cls, token):
        if token == None: return False
        resp = cls.call("/user", token)
        return {
            "temp_name": resp["login"],
            "email": resp["email"]
        }
        
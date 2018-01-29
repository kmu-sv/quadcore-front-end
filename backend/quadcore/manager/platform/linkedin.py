from quadcore.config import Config
from quadcore.manager.platform import Platform

from urllib.parse import urlencode
import requests
import json

class LinkedIn(Platform):
    """
    Manage LinkedIn authentication process.
    """
    base_url = "https://api.linkedin.com/v1"
    authenticate_url = "https://www.linkedin.com/oauth/v2/authorization/?"
    redirect_url = "http://quadcore.news/api/login/linkedin/authorized"
    access_token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    client_id = Config.linkedin_consumer_key
    client_secret = Config.linkedin_consumer_secret
    scope = ["r_basicprofile", "r_emailaddress"]

    @classmethod
    def auth_url(cls, scope=scope, redirect=redirect_url):
        scope_string = str()
        for item in scope:
            scope_string += item + " "

        return cls.authenticate_url + urlencode({
            "response_type": "code",
            "client_id": cls.client_id,
            "redirect_uri": redirect,
            "state": cls.state,
            "scope": scope_string[:-1]
        })

    @classmethod
    def access_token(cls, auth_code, state=str()):
        resp = requests.post(cls.access_token_url, data={
            "grant_type": "authorization_code",
            "client_id": cls.client_id,
            "client_secret": cls.client_secret,
            "redirect_uri": cls.redirect_url,
            "code": auth_code
        }).json()

        return (None if "error" in resp else resp["access_token"])

    @classmethod
    def call(cls, endpoint, token):
        req_header = {
            "Authorization": "Bearer " + token
        }

        return requests.get(cls.base_url + endpoint, 
            headers=req_header).json()

    @classmethod
    def get_auth_info(cls, token):
        if token == None: return None
        resp = cls.call("/people/~:(first-name,email-address)?format=json", token)
        return {
            "username": resp["firstName"],
            "email": resp["emailAddress"]
        }
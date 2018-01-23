import requests
import uuid
from quadcore.config import Config
from urllib.parse import urlencode

class GithubAuthManager:
    """
    Manage Github authentication process.
    """
    # TODO(@harrydrippin) Randomize state string by individual against CSRF attack
    state = str(uuid.uuid4())
    base_url = "https://api.github.com"
    auth_url = "https://github.com/login/oauth/authorize/?"
    access_token_url = "https://github.com/login/oauth/access_token"
    client_id = Config.github_consumer_key
    client_secret = Config.github_consumer_secret

    @classmethod
    def identify_url_generate(cls, redirect, scope=["read:user"], allow_signup=False):
        """
        Generate Github identification url.
        """
        scope_string = str()
        for item in scope:
            scope_string += item + "%20"

        return cls.auth_url + urlencode({
            "client_id": cls.client_id,
            "redirect_uri": redirect,
            "scope": scope_string[:-3],
            "state": cls.state,
            "allow_signup": ("true" if allow_signup else "false")
        })

    @classmethod
    def get_access_token(cls, code, state):
        """
        Get access token from Github.
        """
        req_header = {
            "Accept": "application/json"
        }

        resp = requests.post(cls.access_token_url, data={
            "client_id": cls.client_id,
            "client_secret": cls.client_secret,
            "code": code,
            "state": state
        }, headers=req_header).json()
        
        if "error" in resp:
            return None
        else:
            return resp["access_token"]

    @classmethod
    def call(cls, endpoint, token):
        """
        Fetch JSON with access token from given endpoint.
        """
        req_header = {
            "Authorization": "token " + token
        }

        return requests.get(cls.base_url + endpoint, 
            headers=req_header).json()
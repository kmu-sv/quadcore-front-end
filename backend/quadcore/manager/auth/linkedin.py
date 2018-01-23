import requests
import uuid
from quadcore.config import Config
from urllib.parse import urlencode
import json

class LinkedInAuthManager:
    """
    Manage LinkedIn authentication process.
    """
    # TODO(@royeom) Randomize state string by individual against CSRF attack
    state = str(uuid.uuid4())
    base_url = "https://api.linkedin.com/v1/"
    auth_url = "https://www.linkedin.com/oauth/v2/authorization/?"
    access_token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    client_id = Config.linkedin_consumer_key
    client_secret = Config.linkedin_consumer_secret
    response_type = "code"

    @classmethod
    def identify_url_generate(cls, scope=["r_basicprofile", "r_emailaddress"]):
        """
        Generate Linkedin identification url.
        """
        scope_string = str()
        for item in scope:
            scope_string += item + " "

        return cls.auth_url + urlencode({
            "response_type":cls.response_type,
            "client_id": cls.client_id,
            "redirect_uri": Config.linkedin_redirect_url,
            "state": cls.state,
            "scope": scope_string[:-1]
        })

    @classmethod
    def get_access_token(cls, code):
        """
        Get access token from LinkedIn.
        """

        resp = requests.post(cls.access_token_url, data={
            "grant_type": "authorization_code",
            "client_id": cls.client_id,
            "client_secret": cls.client_secret,
            "redirect_uri": Config.linkedin_redirect_url,
            "code": code
        }).json()

        print(json.dumps(resp, indent=4))
        
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
            "Authorization": "Bearer " + token
        }

        return requests.get(cls.base_url + endpoint, 
            headers=req_header).json()
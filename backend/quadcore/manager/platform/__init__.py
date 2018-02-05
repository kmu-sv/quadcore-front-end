import requests
import uuid
from quadcore.config import Config
from urllib.parse import urlencode
import json

class Platform:
    """
    Platform manager code base.
    """

    # TODO(@harrydrippin) Randomize state string by individual against CSRF attack
    # State string for prevent CSRF attack
    state = str(uuid.uuid4())

    # Base API URL
    base_url = str()

    # OAuth Authorization URL
    auth_url = str()

    # API Redirection URL
    redirect_url = str()

    # Access Token Getting API URL
    access_token_url = str()

    # Client ID for OAuth 2.0 Protocol
    client_id = str()

    # Client Secret for OAuth 2.0 Protocol.
    client_secret = str()
    
    # Permission scope for API connection
    scope = list()

    @classmethod
    def auth_url(cls, scope=scope, redirect=redirect_url):
        """
        Generate platform API identification url.
        Provide scope keyword parameter for setting custom scope if needed.
        """
        return "Not implemented yet!"

    @classmethod
    def access_token(cls, auth_code, state=str()):
        """
        Get access token from platform API.
        Return None if fails.
        """
        return "Not implemented yet!"

    @classmethod
    def call(cls, endpoint, token):
        """
        Fetch JSON with access token from given endpoint.
        """
        return {
            "error": "Not implemented yet!"
        }

    @classmethod
    def get_auth_info(cls, token):
        """
        Fetch user info based on access token.
        Return dictionary when success, None when failure.
        """
        return None
from flask_restful import Resource
from quadcore.parser.github import GithubParser

class Interest(Resource):
    def get(self):
        return GithubParser("token").get_interests(GithubParser.urls)
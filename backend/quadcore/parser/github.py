from quadcore.parser import Parser
import requests

class GithubParser(Parser):
    """
    Interest parser for Github.
    """
    # URLs for parsing user intersts.
    urls = [
        "https://api.github.com/user?type=all&sort=created",
        "https://api.github.com/user/starred"
    ]

    def get_entities_by_sources(self, sources):
        """
        Process entities by Dandelion API.
        """
        return list()
from quadcore.parser import Parser
import requests

class LinkedInParser(Parser):
    """
    Interest parser for LinkedIn.
    """
    # URLs for parsing user intersts.
    urls = []

    def get_entities_by_sources(self, sources):
        """
        Get entities by Dandelion API.
        """
        return list()
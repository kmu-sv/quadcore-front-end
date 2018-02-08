import requests

class Parser:
    """
    Superclass for interest parsers.
    """
    # URLs for parsing user interests.
    urls = list()

    def __init__(self, token):
        """
        Constructor for parsers.
        """
        self.token = token

    def get_interests(self, urls):
        """
        Function for getting interest entities.
        Returns entity ID list.
        """
        sources = self.get_sources(urls)
        interests = self.get_entities_by_sources(sources)
        return interests

    def get_sources(self, urls):
        """
        Fetch sources from given urls.
        Returns given response objects.
        """
        sources = list()
        for url in urls:
            sources.append(requests.get(url))
        return sources

    def get_entities_by_sources(self, sources):
        """
        Get entities by Dandelion API.
        """
        return list()
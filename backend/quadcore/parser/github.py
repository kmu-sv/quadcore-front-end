from quadcore.parser import Parser
import requests

class GithubParser(Parser):
    """
    Interest parser for Github.
    """
    # URLs for parsing user intersts.
    urls = [
        # Fetch contributed, owned repositories.
        "https://api.github.com/user/repos?type=all&sort=created",
        # Fetch starred repositories
        "https://api.github.com/user/starred"
    ]

    def get_entities_by_sources(self, sources):
        """
        Process entities by Dandelion API.
        """
        user_repos, starred_repos = sources[0].json(), sources[1].json()
        return {
            "user_repos": list(map(self.process_repos, user_repos)),
            "starred": list(map(self.process_repos, starred_repos))
        }

    def process_repos(self, data):
        result = {
            "name": data["full_name"]
        }

        result["languages"] = requests.get("https://api.github.com/repos/{name}/languages".format(name=data["full_name"])).json().keys()
        return result
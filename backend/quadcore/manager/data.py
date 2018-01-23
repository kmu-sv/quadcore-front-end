from flask import session
from quadcore.manager.db import DBManager

class DataManager:
    """
    Manage user data on database.
    """
    db = DBManager.get_redis()

    @classmethod
    def get_user_profile(cls, username):
        """
        Fetch user profile based on username.
        If not exist, return None.
        TODO(@harrydrippin): Now not working
        """
        user_key = "user:" + username
        return db.hgetall(user_key)
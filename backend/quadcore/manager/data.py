from quadcore.manager.db import DBManager

class DataManager:
    """
    Manage user data.
    """
    db = DBManager.get_redis()

    @classmethod
    def get_user_profile(cls, email):
        """
        Get user profile from database.
        Return None if not exist.
        """
        return cls.db.hgetall("user:" + email)

    @classmethod
    def update_user_profile(cls, info):
        """
        Update user profile to database.
        """
        if info["username"] == None or info["email"] == None:
            return None
        return cls.db.hmset("user:" + info["email"], info)
    
    @classmethod
    def set_user_profile(cls, info):
        """
        Save user profile to database.
        """
        if info["username"] == None or info["email"] == None:
            return None
        return cls.db.hmset("user:" + info["email"], info)

    @classmethod
    def check_email_username(cls, email):
        """
        Check whether email and username are connected.
        """
        return cls.db.hget('email:' + email, 'username')
        
    # Prepare for case
    # @classmethod
    # def is_exist_user(cls, email):
    #     """
    #     Check this email is already exist in database.
    #     """
    #     return cls.db.keys("user:" + email)

    @classmethod
    def get_user_interests(cls, email):
        """
        Access user:<email> and Fetch interests dict.
        """
        pass
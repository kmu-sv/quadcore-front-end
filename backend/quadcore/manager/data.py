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
        
        # If new info is needed, just add below. 
        return cls.db.hmset("user:" + info["username"], {
            'firstName': info["firstName"],
            'lastName': info["lastName"]
        })
    
    @classmethod
    def set_user_profile(cls, info):
        """
        Save user profile to database.
        """
        if info["username"] == None or info["email"] == None:
            return None
        
        # If new info is needed, just add below. 
        return cls.db.hmset("user:" + info["username"], {
            'email': info["email"],
            'firstName': info["firstName"],
            'lastName': info["lastName"]
        })
    
    @classmethod
    def check_email_username(cls, email):
        """
        Check whether email and username are connected.
        """
        return cls.db.hget('email:' + email, 'username')

    @classmethod
    def set_user_map(cls, info):
        """
        Connect username and email.
        """
        if info["username"] == None or info["email"] == None:
            return None
        return cls.db.hmset("email:" + info["email"], {
            'username': info["username"] 
        })
    
    @classmethod
    def check_username(cls, username):
        """
        Check username in Real-time.
        """
        return cls.db.keys('user:' + username)

    @classmethod
    def get_user_interests(cls, username):
        """
        Access user:<username> and Fetch interests dict.
        """
        pass
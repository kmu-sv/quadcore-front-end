from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Config:
    # Configuration for redis
    redis = {
        "host": os.environ.get("REDIS_HOST"),
        "id": os.environ.get("REDIS_ID"),
        "password": os.environ.get("REDIS_PASSWORD"),
        "port": os.environ.get("REDIS_PORT"),
        "db": os.environ.get("REDIS_DB_NUMBER")
    }

    github_consumer_key = os.environ.get("GITHUB_CONSUMER_KEY")
    github_consumer_secret = os.environ.get("GITHUB_CONSUMER_SECRET")

    linkedin_consumer_key = os.environ.get("LINKEDIN_CONSUMER_KEY")
    linkedin_consumer_secret = os.environ.get("LINKEDIN_CONSUMER_SECRET")
    
    oauth_success_url = "http://quadcore.news/feed.html"
    oauth_signup_url = "http://quadcore.news/profile?signup=1"
    oauth_failure_url = "http://quadcore.news?error=1"
    
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
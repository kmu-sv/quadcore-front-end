import redis

HOST = "localhost"
DB = 0

REDIS_DB = redis.StrictRedis(host=HOST, db=DB, charset="utf-8", decode_responses=True)
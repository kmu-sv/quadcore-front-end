from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Resource, Api
from quadcore.manager.db import DBManager as dm
import random

class Feed(Resource):
    def get(self):
        # Handling this offset on client
        if "offset" not in request.args:
            return {
                "result": 1,
                "cause": "Need to provide proper offset"
            }
        offset = int(request.args["offset"])
        db = dm.get_redis()
        article_count = db.get("article_count")
        article_list = list()
        for i in range(offset, offset + 10):
            article_list.append(db.hgetall("article:" + str(i)))
        return {
            "result": 0,
            "articles": article_list
        }


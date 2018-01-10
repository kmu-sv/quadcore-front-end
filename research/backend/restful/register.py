from manager import dbmanager
from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api
from flask_restful import reqparse
import json
import bcrypt

# url : '/register'
# function : Sign-up with informations about username(e-mail), password, first name and last name.
#            And hashed password enters db
class Register(Resource):

    def get(self):
        return {
            "result": 1,
            "reason": "You approached wrong way!"
        }

    def post(self):
        args = json.loads(request.data.decode("utf-8"))
        username = args['username']
        password = args['password'].encode("utf-8")
        password_check = args['passwordcheck'].encode("utf-8")
        first_name = args['firstname']
        last_name = args['lastname']
    
        if password != password_check:
            raise ValueError('Please confirm password and password check are same')
        else:
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        # Check if input username already exists in DB
        if dbmanager.REDIS_DB.keys('username:' + username):
            raise ValueError('Your username is already being used.')
        else:
            # if not exist, insert in RedisDB
            dbmanager.REDIS_DB.hmset('username:' + username, {
                'password': hashed, 
                'firstname': first_name,
                'lastname': last_name
            })

        # Complete Message
        return {
            'message': 'Sign-up is completed.',
            'username': username,
            'password': str(password),
            'firstname': first_name,
            'lastname': last_name,
            'hashed': str(hashed)
            }

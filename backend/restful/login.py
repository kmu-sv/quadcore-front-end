from manager import dbmanager
from flask import request, session, jsonify, json
from flask_restful import Resource
from .register import Register
import bcrypt

# url : '/login'
# function : Check match of request's password and db's hashed password
class Login(Resource):
    def get(self):
        return {
            "result" : 1,
            "reason" : "You approached wrong way!"
        }
    
    def post(self):
        # Load from Frontend's json
        args = json.loads(request.data)

        # Users enter username & password
        input_username = args['username']
        input_password = args['password'].encode("utf-8")

        # Load password from db
        password_in_db = dbmanager.REDIS_DB.hget('username:' + str(input_username), 'password')

        # Check from input and db
        if bcrypt.checkpw(input_password, password_in_db.encode("utf-8")):
            return {
                "result": 0
            }
        else:
            invalid_response = jsonify({
                "result": 1,
                "cause": "Id or password is invalid!"
             })
            invalid_response.status_code = 401

            return invalid_response

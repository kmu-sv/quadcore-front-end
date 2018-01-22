from flask import session, redirect
from flask_restful import Resource

# url : '/logout'
# function : just redirect to '/'
class Logout(Resource):
    def get(self):
        session.clear()
        return redirect('/')
    
    def post(self):
        session.clear()
        return redirect('/')
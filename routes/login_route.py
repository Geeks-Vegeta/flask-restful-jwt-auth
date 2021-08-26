"""
In this file we are getting user login 
if user login successfully we are sending a jwt token in the header
if user credentials are not matching with database then we are sending
a 404 error 

"""

from flask_restful import Resource, abort, reqparse, marshal_with, fields
from api import db
from db.model import User  # importing user model from db
from passlib.hash import sha256_crypt  #  for checking if password is matching
import jwt  #  creating a token
from api import app
from middleware.islogin import islogin  # middleware for checking if auth is present



# creating a response for json serialization
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "password": fields.String,
    "confirm_password": fields.String
}

# request parameters 
parse = reqparse.RequestParser()
parse.add_argument('email', type=str, help="email required")
parse.add_argument("password", type=str, help="password required")


# login class
class LoginRoute(Resource):

    def post(self):
        args = parse.parse_args()

        # checking if email is present
        user = User.query.filter_by(email=args['email']).first()

        if not user:
            abort(404, message="Invalid email")
        
        # comparing password
        correct_password = sha256_crypt.verify(args['password'], user.password)
        
        # checking passwordbcrypt
        if not correct_password:
            return abort(404, message="password is not correct")

        # creating token if password and email is correct
        token = jwt.encode({'user_id':user.id},app.config['SECRET_KEY'])

        return {'token':token},{'Set-Cookie': f'auth={token}'}

    
    # islogin is an decorator for checking if user is valid
    @islogin
    @marshal_with(resource_fields)
    def get(user_id, self):
        user = User.query.filter_by(id=user_id).first()
        return user,200


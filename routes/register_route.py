"""
register routes class for creating routes regarding users
basically CRUD operation [CREATE, UPDATE, READ, DELETE]

"""

from flask_restful import Resource, marshal_with, fields, reqparse, abort
from api import db
from db.model import User
from passlib.hash import sha256_crypt
from middleware.islogin import islogin


# creating response as a json serialization
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "password": fields.String,
    "confirm_password": fields.String
}


# creating request parameters (query parameters)
parse = reqparse.RequestParser()
parse.add_argument("id", type=int, help="id should be integer")
parse.add_argument("name", type=str, help="name should be string")
parse.add_argument("email", type=str, help="email should be string")
parse.add_argument("password", type=str, help="password should be string")
parse.add_argument("confirm_password", type=str, help="confirm_password should be string")


# register 
class RegisterRoute(Resource):

    # getting all users
    @marshal_with(resource_fields)
    def get(self):

        # getting all users
        user = User.query.all()
        return user,200



    # creating user
    @marshal_with(resource_fields)
    def post(self):
        # getting request from body
        args = parse.parse_args()

        # is email is already present in database
        is_email = User.query.filter_by(email=args['email']).first()
        if is_email:
            abort(404, message="Email is already present try another one")

        #  getting the passwords
        password = args['password']
        confirm_password = args['confirm_password']
        
        #  checking if password is same 
        if password != confirm_password:
            abort(404, message="Password is incorrect")

        # hasging password
        password = sha256_crypt.hash(args['password'])
        
        #  adding users in database
        user = User(name=args['name'], email=args['email'], 
                    password=password, confirm_password=password)
        db.session.add(user)
        db.session.commit()

        return user,200
          
    

    # delete user
    @islogin
    def delete(user_id, self):
       
        # checking if user_id is present
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message=f"User does not exist")
        
        db.session.delete(user)
        db.session.commit()

        return {"message": "deleted successfully"}

    
    # update user
    @islogin
    @marshal_with(resource_fields)
    def put(user_id, self):
        #  this is requrest body
        args = parse.parse_args()

         # checking if user_id is present
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message=f"User does not exist")

        #  changing name
        user.name = args['name']
        db.session.commit()

        return user,200


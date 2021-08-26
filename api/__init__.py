from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = "sdfhs8dhfuijekfodjiujjj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/FlaskLogin'

api = Api(app)
db = SQLAlchemy(app)

from routes.register_route import RegisterRoute
from routes.login_route import LoginRoute
from routes.post_route import PostRoute

api.add_resource(RegisterRoute,"/", "/<user_id>")
api.add_resource(LoginRoute,"/login")
api.add_resource(PostRoute,"/post", "/post/<title_name>")

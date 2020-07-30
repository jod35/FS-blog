from flask import Blueprint,request,jsonify,make_response
from flask_jwt_extended import create_access_token
from main.models.users import User

auth_bp=Blueprint('auth_bp',__name__)

@auth_bp.route('/')
def hello():
    return "Welcome to my auth API"

#######################################
########Authenticate a User############
#######################################

@auth_bp.route('/signin',methods=['POST'])
def authenticate_user():
    data=request.get_json()

    username=data['username']

    password=data['password']

    user=User.query.filter_by(username=username).first()

    if user and user.check_password(password):

        access_token=create_access_token(identity=username)

        message="Logged In as {},your access token is {}".format(username,access_token)
        

        return make_response(
            jsonify(
                {"message":message,
                "Sucess":True}
            )
        )
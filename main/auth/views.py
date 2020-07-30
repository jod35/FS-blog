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
    try:
        data=request.get_json()

        user_candidate=User.query.filter_by(username=data['username']).first()

        if not user_candidate:
            return make_response(
                jsonify({"message":"Invalid Username"})
            )
        
        if user_candidate and user_candidate.check_password(data['password']):

            access_token=create_access_token(identity=data['username'])

            message="Logged In as {}".format(data['username'])

            return make_response(
                jsonify({
                    "message":message,
                    "access_token":access_token,
                    "Success":True,
                })
            )
    except:
        return make_response(
            jsonify({
                "message":"Invalid Login",
                "Success":False
            }),401
        )
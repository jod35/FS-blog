from flask import Blueprint,jsonify,make_response,request
from .models import User,UserOutputSchema

api_bp=Blueprint('api_bp',__name__)

@api_bp.route('/')
def hello():
    return make_response(jsonify({"message":"Hey Welcome to the blog API" }),200)

@api_bp.route('/users',methods=['GET'])
def get_all_users():
    all_users=User.query.all()

    user_schema=UserOutputSchema()

    users=user_schema.dump(all_users)

    return make_response(jsonify({"success":True,
                                    "users":users
                                }))

@api_bp.route('/users',methods=['POST'])
def create_new_user():
    pass

@api_bp.route('/user/<id>',methods=['GET'])
def get_single_user(id):
    pass

@api_bp.route('/user/<id>',methods=['PUT'])
def update_user_info(id):
    pass

@api_bp.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    pass


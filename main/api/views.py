from flask import Blueprint,jsonify,make_response,request
from main.utils.database import db
from .models import User,UserOutputSchema

api_bp=Blueprint('api_bp',__name__)

@api_bp.route('/')
def hello():
    return make_response(jsonify({"message":"Hey Welcome to the blog API" }),200)

@api_bp.route('/users',methods=['GET'])
def get_all_users():
    all_users=User.query.all()

    user_schema=UserOutputSchema(many=True)

    users=user_schema.dump(all_users)

    return make_response(jsonify({"success":True,
                                    "users":users
                                }),201)

@api_bp.route('/users',methods=['POST'])
def create_new_user():
    data=request.get_json()

    new_user=User(username=data['username'],
                    email=data['email'],
                    passwd_hash=data['passwd_hash']    
                                      )
    new_user.hash_password(new_user.passwd_hash)

    new_user.create()

    user_schema=UserOutputSchema()

    user=user_schema.dump(new_user)
    print(user)
    
    return make_response(
        jsonify({"message":"User Resource Created Successfully",
                "Success":True,
                "user":user})
    )


@api_bp.route('/user/<id>',methods=['GET'])
def get_single_user(id):
    single_user=User.query.get_or_404(id)

    user_schema=UserOutputSchema()

    user=user_schema.dump(single_user)

    return make_response(jsonify(
        {"Success":True,
            "user":user,}
    ),200)


@api_bp.route('/user/<id>',methods=['PUT'])
def update_user_info(id):
    data=request.get_json()

    user_to_update=User.query.get_or_404(id)

    if data['username']:
        user_to_update.username=data['username']
    
    db.session.commit()

    user_schema=UserOutputSchema()

    user=user_schema.dump(user_to_update)

    return make_response(
        jsonify(
            {"Success":True,
             "message":"Username modified Successfully",
             "user":user}
        )
    )



@api_bp.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    pass


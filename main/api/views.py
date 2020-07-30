from flask import Blueprint,jsonify,make_response,request
from main.utils.database import db
from main.models.users import User,UserOutputSchema
from main.models.posts import Post,PostOutputSchema

api_bp=Blueprint('api_bp',__name__)
##########################
###### WELCOME ###########
##########################


@api_bp.route('/')
def hello():
    return make_response(jsonify({"message":"Hey Welcome to the blog API" }),200)


##########################
#####GET ALL USERS #######
##########################

@api_bp.route('/users',methods=['GET'])
def get_all_users():
    all_users=User.query.all()

    user_schema=UserOutputSchema(many=True)

    users=user_schema.dump(all_users)

    return make_response(jsonify({"success":True,
                                    "users":users
                                }),201)

###########################
###CREATE NEW USER ########
###########################
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


######################################
#########GET SINGLE USER##############
######################################
@api_bp.route('/user/<id>',methods=['GET'])
def get_single_user(id):
    single_user=User.query.get_or_404(id)

    user_schema=UserOutputSchema()

    user=user_schema.dump(single_user)

    return make_response(jsonify(
        {"Success":True,
            "user":user,}
    ),200)

######################################
######CHANGE USERNAME ################
######################################
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


###############################
###### DELETE USER ############
###############################
@api_bp.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    user_to_delete=User.query.get_or_404(id)

    user_to_delete.delete()

    user=UserOutputSchema().dump(user_to_delete)

    return make_response(
        jsonify({"message":"User Deleted Successfully",
                "user":user})
    )


###########################################################################
######### DONE WITH VIEWS FOR USERS :) ####################################
###########################################################################

################## POST VIEWS #############################################


####################################
#####GET LIST OF POSTS #############
###################################

post_schema=PostOutputSchema(many=True)

@api_bp.route('/posts',methods=['GET'])
def get_all_posts():
    all_posts=Post.query.all()

    posts=post_schema.dump(all_posts)

    return make_response(
        jsonify({"Success":True,
                    "posts":posts}),200
    )

####################################
#####CREATE A BOOK #################
####################################
@api_bp.route('/posts',methods=['POST'])
def create_post():
    data=request.get_json()
    schema=PostOutputSchema()
    new_post=Post(title=data['title'],content=data['content'])
    new_post.create()

    post=schema.dump(new_post)

    return make_response(
        jsonify({"message":"New Post Created Successfully",
                 "Success":True,
                 "post":post}),200
    )



###################################
######GET POST BY ID ##############
###################################
@api_bp.route('/post/<id>',methods=['GET'])
def get_post(id):
    post=Post.query.get_or_404(id)

    schema=PostOutputSchema()

    result=schema.dump(post)

    return make_response(
        jsonify(
            {"Success":True,
            "post":result}
        )
    )


###################################
####### UPDATE post INFO###########
###################################
@api_bp.route('/post/<id>')
def update_post(id):
    pass

###################################
#####DELETE A POST ################
###################################
@api_bp.route('/post/<id>')
def delete_post(id):
    pass
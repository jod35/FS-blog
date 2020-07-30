from flask import Blueprint,jsonify,make_response,request

api_bp=Blueprint('api_bp',__name__)

@api_bp.route('/')
def hello():
    return make_response(jsonify({"message":"Hey Welcome to the blog API" }),200)


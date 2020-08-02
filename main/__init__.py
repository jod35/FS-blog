from flask import Flask,jsonify
from .config import DevConfig
from flask_jwt_extended import JWTManager
from main.utils.database import db
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from flask_migrate import Migrate


app=Flask(__name__)

app.config.from_object(DevConfig)

jwt=JWTManager(app)

db.init_app(app)

migrate=Migrate(app,db)

from main.api.views import api_bp
from main.auth.views import auth_bp


app.register_blueprint(auth_bp,url_prefix='/auth')
app.register_blueprint(api_bp,url_prefix='/api')

@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Resource Not Found"})
    
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message":"Oops, Something went wrong!"})



##########################
# API SPECS ##############
##########################

@app.route('/api/spec')
def spec():
    swag=swagger(app,prefix='/api')
    swag['info']['base']='http://localhost/5000'
    swag['info']['version']='2.0'
    swag['info']['title']='Flask Author DB'
    return jsonify(swag)

swagger_ui_blueprint=get_swaggerui_blueprint('/api/docs','/api/spec',config={'app_name':"Flask Author DB"})

app.register_blueprint(swagger_ui_blueprint,url_prefix='/api/docs')





from main.models.users import User as user_model
from main.models.posts import Post as post_model


@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'user_model':user_model,
        'app':app,
        'post_model':post_model
    }


    



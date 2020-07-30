from flask import Flask,jsonify
from .config import DevConfig
from main.utils.database import db

from flask_migrate import Migrate


app=Flask(__name__)

app.config.from_object(DevConfig)

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


    



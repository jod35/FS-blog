from flask import Flask
from .config import DevConfig
from main.utils.database import db
from main.api.views import api_bp
from main.auth.views import auth_bp
from main.api.models import User as user_model
from main.utils.migrations import migrate
from flask_migrate import Migrate


app=Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)
migrate=Migrate(app,db)



app.register_blueprint(auth_bp,url_prefix='/auth')
app.register_blueprint(api_bp,url_prefix='/api')

@app.errorhandler(400)
def not_found(error):
    return "Page not found"
    
@app.errorhandler(500)
def internal_error(error):
    return "Something went wrong"

@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'user_model':user_model,
        'app':app
    }


    



import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=False
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'mysecretkey'
    SECURITY_PASSWORD_SALT=os.environ.get('PASSWORD_SALT') or 'mysalt'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://jona:nathanoj35@localhost/mydb'
    DEBUG=True
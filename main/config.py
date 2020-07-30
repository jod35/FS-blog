import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=False
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'mysecretkey'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://jona:nathanoj35@localhost/mydb'
    DEBUG=True
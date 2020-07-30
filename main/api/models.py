from main.utils.database import db
from werkzeug.security import generate_password_hash,check_password_hash
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class User(db.Model):
    __tablename__='user_table'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    passwd_hash=db.Column(db.Text,nullable=False)

    def __init__(self,username,email,passwd_hash):
        self.username=username
        self.email=email
        self.passwd_hash=passwd_hash


    def __repr__(self):
        return f'User {self.username}'

    def hash_password(self):
        self.password=generate_password_hash(self.password)

    def check_password(self,password):
        return check_password_hash(self.password,password)


    def create(self):
        db.session.add(self)
        db.session.commit()

class UserOutputSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=User
        sqla_session=db.session

    id=fields.Integer()
    username=fields.String(required=True)
    email=fields.String(required=True)
    passwd_hash=fields.String(required=True)
    
from main.utils.database import db
from datetime import datetime
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Post(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(255),nullable=False)
    content=db.Column(db.Text)
    user_id=db.Column(db.Integer,db.ForeignKey('user_table.id'))
    date_created=db.Column(db.DateTime(),default=datetime.utcnow)

    def __init__(self,title,content,user_id=None):
        self.title =title
        self.content=content
        self.user_id=user_id
        

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    

class PostOutputSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Post
        sqla_session=db.session

    title=fields.String(required=True)
    content=fields.String(required=True)
    user_id=fields.Integer()






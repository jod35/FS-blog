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

    def __init__(self,title,content):
        self.title =title
        self.content=content
        

    def create(self):
        db.session.add(self)
        db.session.commit()


class PostOutputSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Post
        sqla_session=db.session







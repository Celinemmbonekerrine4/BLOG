from flask_login import UserMixin
from . import login_manager




class Blogs(db.Model):
    __tablename__= 'blogs'

     id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    def __repr__(self):
        return f'User {self.name}'
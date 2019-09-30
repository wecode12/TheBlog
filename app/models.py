
from . import db
from app import create_app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from hashlib import md5


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    #creating relationship between users and posts,One User can have many posts
    posts = db.relationship("Posts", backref="user", lazy="dynamic")
    #creating relationship between users and comments,One User can have many comments
    comments = db.relationship("Comments", backref="user", lazy="dynamic")

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
    # pass_secure = db.Column(db.String(255))

class Posts(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title=db.Column(db.String)
    body = db.Column(db.String)
    category = db.Column(db.String(255))
    published = db.Column(db.DateTime,default=datetime.utcnow)
    # Foreign key from users table to link pitches and users
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship("Comments", backref="posts", lazy="dynamic")
    # user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        posts = Posts.query.filter_by(id=id).all()
        return posts

    @classmethod
    def get_category(cls, category):
        category = Posts.query.filter_by(category=category).order_by('-id').all()
        return category

    @classmethod
    def get_all_posts(cls):
        posts = Posts.query.order_by('-id').all()
        return posts
    def __repr__(self):
        return f'Posts {self.body}'

class Comments(db.Model):

    __tablename__ = 'comments'


    id = db.Column(db. Integer, primary_key=True)
    the_comment = db.Column(db.String(255))
    # date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posts_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    def save_comment(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comments = Comments.query.filter_by(post_id=id).all()
        return comments

class Subscribe(db.Model):

    __tablename__='subscribers'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    email=db.Column(db.String(255))

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        subscribers=Subscribe.query.all()
        return subscribers







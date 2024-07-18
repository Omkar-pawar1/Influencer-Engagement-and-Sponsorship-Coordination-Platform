from .database import db

class Influencer(db.Model):
    __tablename__="influencer"
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    name=db.Column(db.String(225),unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(225),default="influencer")
    reach = db.Column(db.Integer)
    ads=db.relationship('Ad_request',backref='influencer', lazy=True)
    category=db.relationship('Category',backref='influencer', lazy=True)

class Sponsor(db.Model):
    __tablename__="sponsor"
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(225),default="sponsor")
    company_name = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    budget = db.Column(db.Float)
    campaigns=db.relationship('Campaign',backref='sponsor',lazy=True)
    ads=db.relationship('Ad_request',backref='sponsor', lazy=True)

class Campaign(db.Model):
    __tablename__="campaign"
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String())
    description=db.Column(db.Text)
    start_date=db.Column(db.Date)
    end_date=db.Column(db.Date)
    budget=db.Column(db.Integer)
    visibility=db.Column(db.Boolean())
    goals=db.Column(db.Text)
    sponsor_id=db.Column(db.Integer,db.ForeignKey('sponsor.id'),nullable=False)

class Ad_request(db.Model):
    __tablename__="ad_request"
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    campaign_id=db.Column(db.Integer,db.ForeignKey('campaign.id'),nullable=False)
    influencer_id=db.Column(db.Integer,db.ForeignKey('influencer.id'),nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable=False)
    message=db.Column(db.Text)
    requirement=db.Column(db.Text)
    payment_amount=db.Column(db.Float)
    status=db.Column(db.String(225))

class Category(db.Model):
    __tablename__="influencer_category"
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    category = db.Column(db.String(255),nullable=False)
    niche = db.Column(db.String(255),nullable=False)
    influencer_id=db.Column(db.Integer,db.ForeignKey('influencer.id'),nullable=False)


# from flask_login import  UserMixin, login_required
# from flask_security import RoleMixin

# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     description = db.Column(db.String(255))

# user_roles = db.Table('user_roles',
#                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# class User(db.Model,UserMixin):
#     __tablename__='user'
#     id = db.Column(db.Integer, autoincrement=True,primary_key=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     roles = db.Column(db.String(225),Default="user")
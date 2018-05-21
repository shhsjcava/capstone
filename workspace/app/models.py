from . import db
from datetime import datetime
from werkzeug.security import check_password_hash

class Users(db.Model):
    userid=db.Column('user_id', db.Integer, primary_key=True)
    fname =db.Column('fname', db.String(20), nullable=False)
    lname =db.Column('lname', db.String(20), nullable=False)
    password = db.Column('password', db.String(80), unique=True)

    def __init__(self, userid, password, lname, fname):
            self.userid = userid
            self.password = password
            self.lname=lname
            self.fname=fname

    def __repr__(self):
            return '<User %r>' % self.userid

# class Players(db.Model):
#     __tablename__ = 'players'
#     pid = db.Column('userid', db.Integer, primary_key=True)
#     password = db.Column(db.String(80), unique=True)
#
#     def verify_password(self, password):
#             """
#             Check if hashed password matches actual password
#             """
#             return check_password_hash(self.password_hash, password)
#
#     def __init__(self, pid, password):
#         self.pid = pid
#         self.password = password
#
#     def __repr__(self):
#         return '<Movie %r>' % self.id
#
#
# class Lecturers(db.Model):
#     __tablename__ = 'lecturers'
#     lid = db.Column('lid', db.Integer, primary_key=True)
#     courseid = db.Column(db.String(80), unique=True)
#
#
# incourse = db.Table('incourse',
#     db.Column('pid', db.Integer, db.ForeignKey('players.pid'), primary_key=True),
#     db.Column('courseid', db.Integer, db.ForeignKey('courses.courseid'), primary_key=True),
#     recentlevel=db.Column(db.String(80), unique=True),
#     topicsdone=db.Column(db.String(80), unique=True),
#     points=db.Column(db.Integer(80), unique=True)
#                     )
#
# class Courses(db.Model):
#     __tablename__ = 'courses'
#     courseid = db.Column('courseid', db.Integer, primary_key=True)
#
#
# class Topic(db.Model):
#     __tablename__ = 'topics'
#     tid = db.Column(db.String, primary_key=True)
#     tpn = db.Column(db.String(), unique=True)
#
#
# class Levels(db.Model):
#     lid = db.Column(db.String, primary_key=True)
#
#
# plays = db.Table('plays',
#                  db.Column('player_id', db.Integer, db.ForeignKey('player.pid'), primary_key=True),
# db.Column('quest_id', db.Integer, db.ForeignKey('questions.qid'), primary_key=True)
# )
#
#
# class Question(db.Model):
#     __tablename__ = 'questions'
#     qid = db.Column(db.String, primary_key=True)
#     soln =db.Column()
#
#     start_time = db.Column(db.DateTime, nullable = False)
#     end_time = db.Column(db.Datetime, nullable=False, default=datetime.now)
#     utopic = db.relationship('Topic', )
#
#     def __init__(self, username, password):
#             self.username = username
#             self.password = password
#
#     def __repr__(self):
#             return '<User %r>' % self.username
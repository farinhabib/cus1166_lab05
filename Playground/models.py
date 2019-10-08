from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app import app
import os
import csv
import sys

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///' + os.path.join(basedir,'app.db')
#
# engine = create_engine(DATABASE_URL)
#
# db = scoped_session(sessionmaker(bind = engine))
#
# db = engine.connect()

# def create_database():
#     db.execute("CREATE TABLE courses (id Integer(10) AUTO_INCREMENT, course_title varchar(30))")

# def list():
#     classes = db.execute("Select* from classes")
#     print("\nCurrent courses in the database\n")
#     for class in classes:
#         print(f"Courses from: {class.course_title}, {classes.id}")



class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String(30), index = True, unique = True)
    course_title = db.Column(db.String(30), index = True, unique = True)

class RegisteredStudent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), index = True, unique = True)
    grade = db.Column(db.String(3), index = True, unique = True)

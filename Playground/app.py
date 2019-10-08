from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Course
from models import db
course1 = ('Software Engineering', 12345)
course2 = ('Data Structures', 26776)
course3 = ('Theory of Programming language', 39967)
course4 = ('Networking', 99678)
course5 = ('Artificial Intelligence', 51189)
classes = [course1, course2, course3, course4, course5]
i = 0
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",classes = classes)

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/add_course", methods = ['POST'])
def add_course():
    if request.method == 'POST':
        courseForm = request.form
        title = courseForm.get('course_title')
        cid = courseForm.get('course_id')
        db.session.add((Course(id = i + 1, course_number = cid, course_title = title)))
    else:
        return render_template("index.html")

@app.route("/register_student/<int:course_id>", methods = ['POST'])
def register_student():
    return render_template("register_student.html")

if __name__ == "__main__":
    app.run()

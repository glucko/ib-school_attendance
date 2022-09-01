from .__init__ import app
from .models import db, Student, Date
from flask import request, render_template, redirect, flash
from datetime import date

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        id = request.form['id']
        stud = Student.query.get(id)

        if stud is None:
            flash("Student not Found")
            return render_template("/index.html")
        d = Date.query.get(date.today())

        if d is None:
            d = Date()
            db.session.add(d)
        stud.dates.append(d)
        db.session.commit()
        flash("Success")
        return render_template("/index.html")

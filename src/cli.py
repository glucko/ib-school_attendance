import click
from flask.cli import with_appcontext
from .models import Student, Date, db


@click.command(name="createdb")
@with_appcontext
def create_db():
    db.create_all()
    db.session.commit()
    print("Database tables created")

@click.command(name="printdb")
@with_appcontext
def print_db():
    users = Student.query.all()

    for user in users:
        print(user.name, user.dates)
        for date in user.dates:
            print(date.date)

@click.command(name="addstudent")
@with_appcontext
def add_student():
    student = Student(name="John smith", email="john.2@bubba.com")
    date = Date()
    student.dates.append(date)
    db.session.add(student)
    db.session.commit()
    print("Student added")
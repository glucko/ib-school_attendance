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
        print(user.id, user.name, user.dates)
        for date in user.dates:
            print(date.date)

@click.command(name="addstudent")
@click.argument("name")
@with_appcontext
def add_student(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    print("Student added")

@click.command(name="cleardb")
@with_appcontext
def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()
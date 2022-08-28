from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table = db.Table(
    "association",
    db.Model.metadata,
    db.Column("student_id", db.ForeignKey("student.id")),
    db.Column("date_id", db.ForeignKey("date.id")),
)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    dates = db.relationship(
        "Date", secondary=association_table, backref="students"
    )

class Date(db.Model):
    __tablename__ = "date"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), unique=True, default=db.func.current_date())
    
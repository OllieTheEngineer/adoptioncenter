from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)


class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.text, nullable=False)
    photo_url = db.Column(db.text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.boolean, nullable=False, default=True)
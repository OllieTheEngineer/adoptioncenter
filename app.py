from flask import Flask, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adoption"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route("/")
def pet_list():
    pet = Pet.query.all()
    return render_template("petlist.html", pet=pet)

@app.route("/add", methods=["GET", "POST"])
def new_pet():

    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo=form.photo.data,
            age=form.age.data,
            notes=form.note.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added.")
        return redirect("/petlist.html")

    else:
      return render_template("pet_form.html", form=form)









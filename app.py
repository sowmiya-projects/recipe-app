from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration (SQLite file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)

# Create database file if not exists
if not os.path.exists('recipes.db'):
    with app.app_context():
        db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        ingredients = request.form["ingredients"]
        steps = request.form["steps"]

        new_recipe = Recipe(name=name, ingredients=ingredients, steps=steps)
        db.session.add(new_recipe)
        db.session.commit()

    recipes = Recipe.query.all()
    return render_template("index.html", recipes=recipes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


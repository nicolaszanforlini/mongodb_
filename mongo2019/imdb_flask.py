from flask import Flask, render_template, request
from wtforms import Form
from flask_wtf import FlaskForm
from pymongo import MongoClient
import pprint

from MongoDB import Film, Actor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', nb_films=Film.get_nb_films(db), nb_actors=Actor.get_nb_actors(db))

@app.route("/films")
def films():
    return render_template('films.html', film_list=Film.title_html(db))

@app.route("/actors")
def actors():
    return render_template('actors.html', actor_list=Film.actors_html(db))

@app.route("/actor")
def actor():
    actor_name = request.args.get('actor_name')
    return render_template('actor.html', actor_name = actor_name, actor_film_list = db.actors.find_one({'name':actor_name}).get('films'))



if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    app.run(host='0.0.0.0', debug=True)

    client.close()

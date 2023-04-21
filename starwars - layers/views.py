from flask import render_template, jsonify
from logic import get_movies, get_characters

def list_movies():
    movies, imgs = get_movies()
    return render_template('index.html', data=movies, imgs=imgs)

def characthers_movies(id):
    characters = get_characters(id)
    if characters is None:
        return jsonify("ID must be less than or equal to 6")
    return render_template('personajes.html',data=characters, id=id)

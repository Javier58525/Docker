import os
from flask import Flask, render_template
import requests
from views import list_movies, characthers_movies

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

movies_url = "https://swapi.dev/api/films/"

app.route("/", methods=['GET'])(list_movies)
app.route("/personajes/<int:id>", methods=['GET'])(characthers_movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)

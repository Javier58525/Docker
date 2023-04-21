import os
from flask import Flask, render_template
import requests

from flask import jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

movies_url = "https://swapi.dev/api/films/"




@app.route("/", methods=['GET'])
def list_movies():
    data = requests.get(movies_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    movies_id =sorted(movies, key=lambda x: x['id'])
    
    return render_template('index.html', data=movies_id)
    
@app.route("/personajes/<int:id>", methods=['GET'])
def characthers_movies(id):
    if id<1 or id > 6 :
        return jsonify("ID must be less than or equal to 6")
    
    data = requests.get(movies_url+ f"/{id}").json()
    characters= data["characters"]
    characters_names=[]
    for character_url in characters:
        character_response = requests.get(character_url)
        character_data = character_response.json()
        character_name = character_data["name"]
        characters_names.append(character_name)

    return render_template('personajes.html',data = characters_names,id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)

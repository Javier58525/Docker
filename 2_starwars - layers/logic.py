import requests

movies_url = "https://swapi.dev/api/films/"

def get_movies():
    data = requests.get(movies_url).json()
    imgs= [
       "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/91NrqPMwWqL._RI_.jpg",
       "https://http2.mlstatic.com/D_NQ_NP_735560-MLM49374370643_032022-O.jpg",
       "https://m.media-amazon.com/images/I/71OAJeaOCEL.jpg",
       "https://m.media-amazon.com/images/I/91YXgocJn5L.jpg",
       "https://m.media-amazon.com/images/I/91eOgodm4nL.jpg",
       "https://m.media-amazon.com/images/I/81g8vEs4ixL.jpg"
      ]
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    return (sorted(movies, key=lambda x: x['id']),imgs)

def get_characters(id):
    if id<1 or id > 6 :
        return None
    
    data = requests.get(movies_url+ f"/{id}").json()
    characters= data["characters"]
    characters_names=[]
    for character_url in characters:
        character_response = requests.get(character_url)
        character_data = character_response.json()
        character_name = character_data["name"]
        characters_names.append(character_name)

    return characters_names
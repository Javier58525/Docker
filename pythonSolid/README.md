# Analiza el funcionamiento del script
¿Cual es su entrada?

La URL del sitio web http://www.imdb.com/chart/top es la entrada del script.

¿Que procesamiento esta haciendo?
1. Hace un request a http://www.imdb.com/chart/top

2.Con beautifulSoup analiza y obtiene la información deseada: el título, año, clasificación, votos, enlace.

3.Ya abtenida la información la guardamos en diccionarios y  la lista se guarda en un archivo csv.

¿Cual es su salida?

La salida es un archivo CSV llamado movie_results.csv que contiene los detalles de las 250 películas mejor calificadas.


# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME
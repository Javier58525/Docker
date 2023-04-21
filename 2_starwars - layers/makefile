.DEFAULT_GOAL := build

build:
	docker build -t my-flask-app .
.PHONY: build

run:
	docker run -p 8000:8000 my-flask-app
.PHONY: run

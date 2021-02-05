SHELL := /bin/bash

makessh:
	docker exec -it blogapp /bin/bash

makeserver:
    python manage.py runserver

runflake8:
	flake8 /users

runtests:
	py manage.py test	

makebuild:
    docker-compose build
    docker-compose up -d

makeup:
	docker-compose up

down:
    docker-compose down
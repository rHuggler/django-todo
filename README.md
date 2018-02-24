# django-todo
This is a simple to-do list application divided in two parts: a RESTful API and a Web Application client.

#### Technologies
- Vue.js 2.5.2
- Python 3.6.4
- Django 2.0.2
- django-rest-framework 3.7.7
- PostgreSQL 10.2

#### Running with Docker

Building app image:
```sh
    docker-compose build
```

Setting the database up:
```sh
    docker-compose run api python manage.py makemigrations
    docker-compose run api python manage.py migrate
```

Installing npm modules:
```sh
    docker-compose run web npm install
```

Cleaning up:
```sh
    docker-compose down
    docker-compose rm -f --all
```

Running the app:
```sh
    docker-compose up
```

Access the browsable API at [http://localhost:8000](http://localhost:8000).
Access the web client at [http://localhost:8080](http://localhost:8080).

Bring the app down:
```sh
    docker-compose down
```

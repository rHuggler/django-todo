# django-todo
This is a simple to-do list RESTFul API.

#### Technologies
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


Bring the app down:
```sh
    docker-compose down
```

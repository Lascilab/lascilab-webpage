#!/bin/bash
docker-compose build
docker-compose up -d
# docker-compose exec web ./manage.py migrate
# docker-compose exec web ./manage.py collectstatic --noinput 
# docker-compose exec web ./manage.py createsuperuser

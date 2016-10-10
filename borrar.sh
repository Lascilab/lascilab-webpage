#!/bin/bash
docker-compose stop
docker-compose rm -f
docker ps -a
docker volume ls
docker volume rm $(docker volume ls -qf dangling=true)

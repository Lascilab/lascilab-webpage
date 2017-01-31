#!/bin/env bash

# creating a user for database in postgres container
psql -U postgres -c "CREATE USER $DB_USER PASSWORD '$DB_PASS'"
# creating a database for the postgres user created
psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER"

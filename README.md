# Large Scale Infraestructure Laboratory

<p align="center">
<img src="https://avatars2.githubusercontent.com/u/20485166?v=3&s=200" width="150"/> 
</p>

This is the source code of the "Lascilab" webpage, it was wrote using python3.6+.

## For deploy in production
Install Docker and Docker Compose.

```bash
docker-compose build
```

```bash
docker-compose up -d
```

when the web service is ready, use the following command to load the static files for the admin page.

```bash
docker-compose exec web ./manage.py collectstatic
```

to load the initial data of the database use the following command.

```bash
docker-compose exec web ./manage.py loaddata db.json
```

## For Development

### Configure you machine

Assuming you're on debian like OS

```bash
sudo apt-get update
sudo apt-get install python-dev python-pip libpq-dev
sudo pip install virtualenv virtualenvwrapper requests[security]
```

locate in the *webpage* directory and perform the following commads to setup the development virtualenv.

```bash
mkvirtualenv --python=python3.6 .env
```

activate the development environment 

```bash
source .env/bin/activate
```

install the app requirements. 

```bash
pip3.6 install -r dev_req.txt
```

if the python virtual environment is active, use the following command to deactivate it.

```bash
deactivate
```

create data base migrations. **Note: every time you change a model you have to perform "makemigrations" and "migrate" in order to apply the changes to the database**.

```bash
./manage.py makemigrations
```

apply migrations changes into the database.

```bash
./manage.py migrate
```

to run the development server.

```bash
./manage.py runserver 0.0.0.0:8000
```

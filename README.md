# Network-lab
<p align="center">
<img src="https://avatars2.githubusercontent.com/u/20485166?v=3&s=200" width="250"/> 
</p>

This is the source code of the "Laboratorio de redes y sistemas distribuidos" webpage, it was wrote using python2.7+.

## For deploy in production
Install Docker and Docker Compose. If you want to restore the data backup, use the following command.

```bash
docker-compose exec web ./manage.py loaddata backup.json
```

If the migration command fails, wait at least 1m (while mysql starts) and re-run the command

## For Development

### Configure you machine
Assuming you're on debian like OS

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python-dev python-pip
sudo pip install virtualenv virtualenvwrapper requests[security]

source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv network_lab
```

now, go to project folder and then run

```bash
cd webpage
pip install -r requirements-dev.txt
workon network_lab
./manage.py runserver
```

then, in your browser, go to localhost:8000

### Posting data
We're using a sqlite database for dev so if you want to insert any data, please go to localhost:8000/admin

| username |   password   |
|----------|--------------|
| lascilab | lascilab2015 |

### Modifying templates
If you're not familiar with django template system, take a look  [here](https://docs.djangoproject.com/en/1.8/topics/templates/)

Now, all static data is in static folder, by now where just have css folder inside, but you can add whatever you want (i.e js, img, plugins, fonts, etc)


Where using template's inheritance, base.html is located at templates/base.html.

Every single app has his own templates folder, and is located at appfolder/templates/appname

### Modifying models
If you're not familiar with django model system, take a look 
[here](https://docs.djangoproject.com/en/1.8/topics/db/models/)

If you want to make changes to models, and reflex in database, please do
```
./manage.py makemigrations appname
./manage.py migrate
```

Enjoy Coding!


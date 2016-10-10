# network-lab

OS requirements python2.7+, pip

#We've migrated to [here](https://github.com/Lascilab/lascilab-webpage)

##Configure you machine
Assuming you're on debian like OS
```
sudo apt-get update && sudo apt-get upgrade # Upgrade your system
sudo apt-get install python-dev python-pip #install Python Dev Tools and Python Package Manager
sudo pip install virtualenv virtualenvwrapper  # Install virtualenv
source /usr/local/bin/virtualenvwrapper.sh # add virtualenv functions to path
mkvirtualenv network_lab # create virtualenv
pip install -r requirements.txt # install requirements
```

if you get this error
```
InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail.
```
Use this command
```
pip install requests[security]
```

now  go to project folder and then

`./manage.py runserver`

now in your browser go to localhost:8000

## Posting data
We're using a sqlite database, if you want to insert any data, please go to localhost:8000/admin

username: lascilab
password: lascilab2015

## Modifying template
If you're not familiar with django template system, take a look  [here](https://docs.djangoproject.com/en/1.8/topics/templates/)

Now, all static data is in static folder, by now where just have css folder inside, but you can add whatever you want (i.e js, img, plugins, fonts, etc)


Where using template's inheritance, base.html is located at templates/base.html.

Every single app has his own templates folder, and is located at appfolder/templates/appname

## Modifying template
If you're not familiar with django model system, take a look 
[here](https://docs.djangoproject.com/en/1.8/topics/db/models/)

If you want to make changes to models, and reflex in database, please do
```
./manage.py makemigrations appname
./manage.py migrate
```

Please: **DO NOT REMOVE MIGRATIONS FOLDERS!!!**

if migration proccess wont work, take a look to error log, is porobably an error to blame yourself 
> Tip: if you'rea adding a new field, use `blank=True, null=True` to avoid null reference database errors

Enjoy Coding!


# network-lab

OS requirements python2.7+, pip

##Configure you machine
Assuming you're on debian like OS
```
sudo apt-get update && sudo apt-get upgrade # Upgrade your system
sudo apt-get install python-dev python-pip #install Python Dev Tools and Python Package Manager
sudo pip install virtualenv virtualenvwrapper  # Install virtualenv
source /usr/local/bin/virtualenvwrapper.sh # add virtualenv functions to path
mkvirtualenv network_lab # create virtualenv
pip install requirements.txt # install requirements
```

now  go to project folder and then

`./manage.py runserver`

now in your browser go to localhost:8000

## Posting data
We're using a sqlite database, if you want to insert any data, please go to localhost:8000/admin

username: lascilab
password: lascilab2015


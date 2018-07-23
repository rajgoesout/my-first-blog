# my-first-blog

This is a blog application made using Django.

## Getting Started
* Clone this repo
* Install python3 if you haven't already
* ```cd``` into ```my-first-blog```
* Create a virtual environment: ```python -m venv venv``` (Note: write ```python3``` instead of ```python``` on mac)
* Activate virtual environment: ```source venv/bin/activate```
* ```pip install django```
* ```python manage.py migrate```
* ```python manage.py runserver```
* Now the server should start working: open your favorite browser and go to http://127.0.0.1:8000/

## Creating admin account
* ```python manage.py createsuperuser```
* Now enter your desired username, email and password
* Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and login
* Here you'll be able to add/edit/delete posts.
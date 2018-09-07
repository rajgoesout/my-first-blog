# my-first-blog

This is a blog application made using Django.
You can find the live blog here: [Rajdeep's Blog](https://rajdeepbharati.pythonanywhere.com)

## Getting Started
* Clone this repo
* Install [Python 3.7](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/) if you haven't already
* ```cd``` into ```my-first-blog```
* Create a virtual environment: ```python -m venv venv``` (Note: write ```python3``` instead of ```python``` on mac)
* Activate virtual environment: ```source venv/bin/activate```
* ```pip install Django==2.1```
* ```python manage.py migrate```
* ```python manage.py runserver```
* Now the server should start working: open your favorite browser and go to http://127.0.0.1:8000/

## Using the application
* Open another terminal/command line window and activate ```venv``` after going into to root directory (```my-first-blog```)
* ```python manage.py createsuperuser```
* Now enter your desired username, email and password
* Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and click on the lock button and login with your credentials.
* Click '+' button to create a new post, hit save. Now your post will be saved as a Draft.
* Click Edit button (next to '+') to view drafts. You may edit, publish or delete your drafts.
* Head to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and Voila! you'll be able to see a list of your published posts.
* Users may add comments to your posts, and you have to approve or disapprove each comment in order to make the comment available to the public.
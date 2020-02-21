# URL-Status-Checker
URL Status Checker
## Task description:
Implement URL Status Checker  
Django project git repository with applications code that:  
- Allow store and manipulate with set of URL (stored in DB, using django ORM), manipulation (add/delete) via Django admin.  
- Simple view for authenticated users, that shows list of added URLS, monitors url HTTP response status (using Ajax request to server), lets choose check interval, pause individual links check  
- On ajax request, server should check (in async) all users links listed in db and return HTTP status code of urls (200 - green row in list, other - red row in list).  


## How to run:  
Clone this repo and cd to it.  
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Go to [app](http://localhost:8000/)

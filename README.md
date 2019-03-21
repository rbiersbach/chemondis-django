# Django Tutorial

## Django project and application

Check django version

    python -m django --version
    
Create a django project
    
    django-admin startproject chemondis
     
Run the server
 
    python manage.py runserver

First available route

    http://127.0.0.1:8000/admin
    
Create an app

    python manage.py startapp polls
    
## Database handling

Migrate to database

    python manage.py migrate
     
Make migrations

    python manage.py makemigrations polls 
    
Show sql of certain migration

    python manage.py sqlmigrate polls 0001
    
Using the shell
    
    python manage.py shell
    
## Administration

Create a user

    python manage.py createsuperuser
    
    
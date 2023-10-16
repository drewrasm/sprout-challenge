# sprout-challenge

## project structure

- sprout - django project
- urlparser - django app for handling the shortened url creation and redirects

## get up and running

- use a form of environment like pyenv
- download dependencies
  - pip install -r requirements.txt
- run migrations
  - python manage.py migrate
- run server
  - python manage.py runserver

## Notes:

- In one of the specifications it says "Store and retrieve the Short URLS using the Django ORM, and by creating a model for them." I opted to use a serializer for that, but it ends up using the Django ORM. I'm assuming that will fill the requirement.

# libby-django-restapi-graphql
Django REST Framework API and a Graphene GraphQL interface built with REST API serializers

## About
Simple library backend using Django REST Framework and Graphene to create a REST API and a GraphQL interface. The stack is Python/Django/SQLite/GraphQL/Graphene/Django REST Framework. You can see working example here:

REST API:
  - Functionality:
    - 
  - pagination example

GraphQL:

## Features
Book:
  - Add Book
  - Update Book
  - Delete Book
  - View Book Details
  
Author:
  - Add Author
  - Update Author
  - Delete Author
  - View Author Details

## Install
Install Dependencies (in same folder as Pipfile):

    pipenv install 
    
## Setup
DB Settings:
- Add your DB details to settings.py

DB Migrations:

    python manage.py migrate
    
## Run
Start server:

    python manage.py runserver

## TODO
- unit tests
- integration tests

# Backend

Start new Django project
django-admin startproject backend

Make a Django app
python manage.py startapp api

## JWT Token
Permission or authentication. Frontend and backend are separate. The request to the backend will include the JWT to tell the backend who is interacting with them.
The backend grants an access token and a refresh token. Frontend will store both. When access token expires, the frontend will submit the refresh token to the backend which will return another access token.

## Serializer
Django uses ORM (maps Python object to database operations). Our API uses JSON (standard format for website applications), eg to accept username and password. A serializer converts into JSON and vice versa.

## Migration
Create the files to specify the migration
python manage.py makemigrations

Migrate - aka provision the database so it has the right tables
python manage.py migrate

## Run app
python manage.py runserver

### See users
Go to http://127.0.0.1:8000/api/user/register/ and register a user
Go to http://127.0.0.1:8000/api/token/, log in and see the access and refresh tokens
The refresh token can be pasted in http://127.0.0.1:8000/api/token/refresh to obtain a new access token

# Frontend
For react:
npm create vite@latest frontend -- --template react
npm install axios react-router-dom jwt-decode

# Deploy
Using https://wso2.com/choreo/

## Database
Need to get Host, Name, etc from host platform. Change accordingly in settings.py
Rerun python manage.py migrate to connect to the remote database

## Backend

## Frontend
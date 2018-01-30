# iShelf API

iShelf API Sample.

## Features

1. Administration panel
2. Filtering data in administration panel
3. Editable forms in administration panel
4. Browsable API
5. Swagger documentation
6. Basic authentication
7. Permissions
8. Pagination
9. Field-based filters in URLs
10. Sample CRUD endpoints
11. Localization
12. Various serializations: JSON, JSONP, XML, YAML

## Backend management

1. Create virtual environment:

    > virtualenv .venv -p python3

2. Activate virtual environment:

    > source .venv/bin/activate

3. Install requirements

    > pip install -r requirements.txt

## Database synchronization

1. When executing server for the first time, you have to synchronize database (and execute migrations):

    > python manage.py migrate

2. Load sample data:

    > python manage.py loaddata quickstart_<authors/books>

## Running server

1. Make sure the virtual environment has been activated:

    > source .venv/bin/activate

2. Start server by typing:

    > python manage.py runserver \<address\>:\<port\>

- I.e. start server at port 8000 to listen for connections from whatever source:

    > python manage.py runserver 0.0.0.0:8000

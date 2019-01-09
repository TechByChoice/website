# Tech By Choice website

## created with [wagtail](https://wagtail.io/)

## Installation instructions:

## Requirements

* Python 3
* Pipenv
* PostgreSQL 10


### Install Python and pipenv and enter virtual environment:

On macOS system the easiest way to do it is to use homebrew package manager. This command will install latest Python version:

    $ brew install python

Install pipenv:

    $ pip3 install pipenv

Start a shell with virtual env loaded:

    $ pipenv shell

Next step is to install all the required packages. This project is using `Pipenv` to manage dependencies:

    $ pipenv install

`Pipenv` automatically creates virtual environment using Python version specified in
`Pipfile` and installs all dependencies.


### Start the app

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

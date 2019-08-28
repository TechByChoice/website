# Tech By Choice website

## created with [wagtail](https://wagtail.io/)

More deployment info found here: [Wagtail/Heroku deployment guide](https://wagtail.io/blog/wagtail-heroku-2017/)

Check out the [admin panel](https://www.techbychoice.org/admin)
Ask vanessa@techbychoice.org for:
- .env credentials
- production login credentials

## Local Development Installation instructions:

## Requirements

- Python 3.6.x
- Postgresql 10.x (Production version)
  - You can check the current version of our postgres db on heroku cli with: `heroku pg:info -a [production-app-name]`
	- More information about what versions of postgres Heroku supports here: https://devcenter.heroku.com/articles/heroku-postgresql#version-support-and-legacy-infrastructure
- Heroku credentials: Ask vanessa@techbychoice.org for access to the staging and/or production Heroku apps


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

### Set up database
$ createdb tbc_db

### Set up your .env
Create a .env file in your project root and copy the contents of the [example .env](https://github.com/TechByChoice/website/blob/develop/.env.example) into your new .env file
Ask vanessa@techbychoice.org for credentials/keys

### Start the app

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py compress
    $ python manage.py runserver

Your instance is up and running! Available on **http://localhost:8000**

Log into the admin panel with your createsuperuser info to create pages and customize: **http://localhost:8000/admin**

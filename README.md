# Python Boilerplate

## Requirements
+ Python 3
+ Mongodb
+ Virtualenv
+ check requirements.txt for additional libraries needed

## References
+ [Flask](http://flask.pocoo.org/)
+ [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)
+ [Coverage](https://coverage.readthedocs.io/)
+ [PyTest](https://docs.pytest.org/en/latest/)
+ [PyTest-Cov](https://pytest-cov.readthedocs.io/en/latest/)
+ [PyTest Flask](http://pytest-flask.readthedocs.io/en/latest/)
+ [Arrow](http://arrow.readthedocs.io/en/latest/)
+ [Ldap3](http://ldap3.readthedocs.io/)
+ [Swagger](https://swagger.io/docs/)
+ [Flask-mongoengine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

## How to run the app?

1. Virtualenv
    + create virtualenv inside the folder

        `virtualenv --python=python3 venv`
    + activate virtualenv

        `source venv/bin/activate`
    + install the requirements

        `pip install -r requirements.txt`
    + create *.env* from *.env.example* and configure it

        `cp .env.example .env`
    + run server

        `python manage.py server`


## How to run test?

1. Run test

    `py.test --cov=app`
2. Run code coverage

    `coverage report -m`

## Api Documentation

+ edit `app/static/swagger.json`
+ open `{base_url}/api/docs`

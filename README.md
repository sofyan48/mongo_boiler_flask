# Python Boilerplate

## Requirements
+ Python 3
+ MySQL/MariaDb
+ Virtualenv
+ check requirements.txt for additional libraries needed

## References
+ [Flask](http://flask.pocoo.org/)
+ [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)
+ [Flask-MySQLDB](http://flask-mysqldb.readthedocs.io/en/latest/)
+ [Coverage](https://coverage.readthedocs.io/)
+ [PyTest](https://docs.pytest.org/en/latest/)
+ [PyTest-Cov](https://pytest-cov.readthedocs.io/en/latest/)
+ [PyTest Flask](http://pytest-flask.readthedocs.io/en/latest/)
+ [Arrow](http://arrow.readthedocs.io/en/latest/)
+ [Ldap3](http://ldap3.readthedocs.io/)
+ [Swagger](https://swagger.io/docs/)

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
2. Docker
    + build the image

        `docker build -t boilerplate:latest .`
    + Run a command in a new container (change the port accordingly)

        `docker run -d -p 5151:5151 boilerplate`
 
## How to run test?

1. Run test

    `py.test --cov=app`
2. Run code coverage
    
    `coverage report -m`

## Api Documentation

+ edit `app/static/swagger.json`
+ open `{base_url}/api/docs`
## Tips

### Access mysql on host from docker container
- edit *my.cnf*, uncomment this line and save the file

    `bind-address = 0.0.0.0`
- create new user on mysql to allow remote connection (edit to suit yours)

    ```
    CREATE USER 'newuser'@'%' IDENTIFIED VIA mysql_native_password USING '***';GRANT USAGE ON *.* TO 'newuser'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;GRANT ALL PRIVILEGES ON `databasename`.* TO 'databasename'@'%';
    ```
- check host ip address used by docker (usually docker0), and look at *inet addr*

    `ifconfig docker0`
- change the configuration based on displayed ip, for example : **172.17.0.1**
- rebuild the docker and run it
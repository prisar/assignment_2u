Steps I followed:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT

3) Create superuser for with admin role for the application

    $ python manage.py createsuperuser

4) Install postgresql

    $ sudo apt-get update

    $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

5) Install psycopg2

    $ sudo pip install psycopg2

6) Start service

    $ sudo service postgresql start

7) Create database and role

    $ sudo su - postgres
    $ psql
    $ CREATE DATABASE udaan;
    $ CREATE USER udaanuser WITH PASSWORD 'password';
    $ ALTER ROLE udaanuser SET client_encoding TO 'utf8'; 
    $ ALTER ROLE udaanuser SET default_transaction_isolation TO 'read committed'; 
    $ ALTER ROLE udaanuser SET timezone TO 'UTC';
    $ GRANT ALL PRIVILEGES ON DATABASE udaan TO udaanuser; 
    
8) Query Database

    $ psql -h localhost -d udaan -U udaanuser -W
    $ \q


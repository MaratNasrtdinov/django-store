<p align="center">
 <h1>Store</h1>
</p>



## About
An example of an online store on Django with a payment system, authentication, shopping cart, REST API, etc,.

Located on the server at: http://84.38.180.112/

The following technologies were used during creation: django, django rest framework, redis, celery, OAuth, PostgreSQL, stripe, smtp.yandex, nginx, gunicorn .


## Installation

1. Сreate and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install the libraries:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Make migrations, load the fixtures and start the server
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
   
4. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
   
5. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```




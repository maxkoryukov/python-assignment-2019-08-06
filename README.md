# python-assignment-2019-08-06

Django App: **pythonassignment**

Repository URL: https://github.com/maxkoryukov/python-assignment-2019-08-06

## HOWTO RUN THE DEMO

First of all, get the sources.

### Prerequisites

To run the demo application you will need `docker` and `docker-compose`, because
the application consists of 4 services:

* celery app
* Django app
* Django database
* celery broker-database (_redis_ in this case)

### Step by step

1. Prepare DB by running:
	```
	docker-compose run web.local python manage.py migrate
	```
2. Run the app:
	```
	docker-compose up
	```

All services should start.

After tests just run `docker-compose down` to clean up everything.

**!!! Important !!!**

Sometimes Postgres takes too long to start, so the web-service (Django), which
depends on the DB, fails to start. I don't know about simple solutions for this
issue (`docker-compose` has `depends_on` option, but it is the order of
**starting** containers **not waiting**; and `postgres`-container returns
control earlier than DB is really initialized and ready to accept connections).

## Test API

OK, let's suppose that all the services are running. So, now we could test
the API.

All endpoints are listed on the main page: **http://localhost:8000/api/**

A little bit more details in the next chapters

### List all saved exceptions

**http://localhost:8000/api/service-error/**

Just open this URL in your browser — it will send the **GET** request and API
will return the list of exceptions.

`curl` command:

```
curl -X GET http://localhost:8000/api/service-error/
```

### Raise a new exception

**http://localhost:8000/api/raise-error/**

Just open this URL in your browser — it will send the **GET** request and the
code of the URL-handler will raise an `Exception` (propagated further).

`curl` command:

```
curl -X GET http://localhost:8000/api/raise-error/
```

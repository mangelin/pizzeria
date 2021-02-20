### Setting up

```
$ pip install -r requirements.txt
```

### Running test

```
$ python -m unittest
```

### Code coverage

To check code coverage, type the following command:

```
$ coverage run -m unittest
```

To generate coverage report type the following command:

```
$ coverage report -m
```

## Docker

build the container:

```
$ docker-compose -f dev.yml build
```

run tests:

```
$ docker-compose -f dev.yml run --rm pizzeria python -m unittest
```

and code coverage:

```
$ docker-compose -f dev.yml run --rm pizzeria coverage run -m unittest

$ docker-compose -f dev.yml run --rm pizzeria coverage report -m
```

## Running container

To run the developement container you havo to use docker-compose:

```
$ docker-compose -f dev.yml run --rm pizzeria
```

The production container can be executed directly using
docker command:

```
$ docker run pizzeria-prd:0.1-alpine
```
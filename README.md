# Markpad
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CircleCI](https://circleci.com/gh/rafaellcoellho/markpad-api.svg?style=svg&circle-token=9015714b9f17c89769c53388e3c4c71c532b2db0)](https://circleci.com/gh/rafaellcoellho/markpad-api)

A notepad in the web with markdown.

# Setup enviroment

## virtualenv

Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/]) and run:

```bash
$ mkvirtualenv --python=python3.6 markpad-api
```

To activate the virtual env just:

```bash
$ workon markpad
```

## Dev enviroment

Create a enviroment file, example:
```
MONGO_URI=mongodb://database:27017
MONGO_DATABASE_NAME=markpad
FRONTEND_ORIGIN=http://localhost:8080
```

Use makefile:
```bash
$ make -B run_local
```

## Tests

```bash
$ make -B tests
```

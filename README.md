<p align="center">
  <a href="https://markpad.com.br" target="_blank" rel="noopener noreferrer">
    <img alt="Logo" src="./logo.jpg" width="600px">
  </a>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT Licence"></a>
  <a href="https://circleci.com/gh/rafaellcoellho/markpad-api"><img src="https://circleci.com/gh/rafaellcoellho/markpad-api.svg?style=svg&circle-token=9015714b9f17c89769c53388e3c4c71c532b2db0" alt="Circle CI"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://codecov.io/gh/rafaellcoellho/markpad-api/branch/master/graph/badge.svg" alt="codecov"></a>
  <a href="https://codeclimate.com/github/rafaellcoellho/markpad-api/maintainability"><img src="https://api.codeclimate.com/v1/badges/887fd0726fc0d43ef168/maintainability" alt="Maintainability"></a>
</p>

Backend of a notepad in the web with markdown.

# Setup enviroment

## virtualenv

Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/]) and run:

```bash
$ mkvirtualenv --python=python3.6 markpad-api
```

To activate the virtual env just:

```bash
$ workon markpad-api
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

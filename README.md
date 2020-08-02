<p align="left">
  <a href="https://markpad.com.br" target="_blank" rel="noopener noreferrer">
    <img alt="Logo" src="./logo.png" width="300px">
  </a>
</p>

<p align="left">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT Licence"></a>
</p>

__No longer maintained!__

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
MONGODB_URI=mongodb://database:27017
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

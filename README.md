# Markpad

A notepad in the web with markdown.

# Setup enviroment

## virtualenv

Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/]) and run:

```bash
$ mkvirtualenv --python=python3.6 markpad
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
```

Use makefile:
```bash
$ make -B run_local
```

## Tests

```bash
$ make -B tests
```

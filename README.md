# Markpad

A notepad in the web with markdown.

# Setup enviroment

## virtualenv

Install (virtualenvwrapper)[https://virtualenvwrapper.readthedocs.io/en/latest/] and run:

```bash
$ mkvirtualenv --python=python3.6 markpad
```

To activate the virtual env just:

```bash
$ workon markpad
```

## Dev enviroment

```bash
$ docker-compose up
```

## Tests

```bash
$ sh run_tests.sh
```
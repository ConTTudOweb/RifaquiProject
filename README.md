# Rifaqui Project

Rifaqui is online system for raffle.

[![Build Status](https://travis-ci.org/ConTTudOweb/RifaquiProject.svg?branch=master)](https://travis-ci.org/ConTTudOweb/RifaquiProject)
[![Coverage Status](https://coveralls.io/repos/github/ConTTudOweb/RifaquiProject/badge.svg?branch=master)](https://coveralls.io/github/ConTTudOweb/RifaquiProject?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c44b09f7d30c31f5c39/maintainability)](https://codeclimate.com/github/ConTTudOweb/RifaquiProject/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3c44b09f7d30c31f5c39/test_coverage)](https://codeclimate.com/github/ConTTudOweb/RifaquiProject/test_coverage)

## How to develop?

01. Clone the repository;
02. Create a "virtualenv" with Python 3.6;
03. Activate the "virtualenv";
04. Upgrade the "pip";
05. Install the dependencies;
06. Configure the instance with the ".env";
07. Run the tests;
08. Create DataBase;
09. Create Super User;

```console
git clone git@github.com:ConTTudOweb/RifaquiProject.git
cd RifaquiProject
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
python manage.py migrate
python manage.py createsuperuser
```

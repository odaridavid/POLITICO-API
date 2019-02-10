# POLITICO-API
**POLITICO API** Is a pure Flask REST API app that serves endpoints for political parties,government offices,
petitioning,voting and user login and sign up to be consumed by front end frameworks.

!['PythonVersion''](https://img.shields.io/badge/python-3.6.7-yellow.svg)
!['License'](https://img.shields.io/badge/License-MIT-green.svg)
!['Travis'](https://travis-ci.org/Davidodari/POLITICO-API.svg?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/4151dd7acdb2ddb19f1f/maintainability)](https://codeclimate.com/github/Davidodari/POLITICO-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Davidodari/POLITICO-API/badge.svg?branch=ch-refactor-tests-163807952)](https://coveralls.io/github/Davidodari/POLITICO-API?branch=ch-refactor-tests-163807952)

### Endpoints

|   ENDPOINT  | METHOD | STATUS |
|:---:|:---:|:---:|
| /offices                |  GET     |  Gets List of offices |
| /offices                |  POST    |  Adds an office to List of offices  |
| /parties                |  GET     |  Gets List of Parties  |
| /parties                |  POST    |  Adds a party to list of parties  |
| /parties/<party_id>     |  GET     |  Gets a specific party  |
| /parties/<party_id>/name|  PATCH   |  Updates Name value of a party  |
| /parties/<party_id>     |  DELETE  |  Deletes Specified Party |
| /offices/<offices_id>   |  GET     |  Gets a specific office |
| /users                  |  POST    |  Adds User to List Of Users  |


## Author

[David Odari](https://github.com/Davidodari)

## Testing and Running Of App

##### Heroku

App Link Hosted On Heroku

[POLITICO-API on Heroku](https://blackpolitico-api-heroku.herokuapp.com/)

1. Append Endpoints to the the above link and try out Get methods

##### Local Machine

1. From your terminal clone The Repository on your machine \
   `git clone repo link `
2. Checkout to `Develop Branch`
3. Start virtual env if is installed or check out [documentation](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments) to set it up\
  Since Project was built on python 3
  `. venv/bin/activate`  
4. Run Flask App
   - First run the following commands to set up the environment and config
      - export FLASK_APP=run.py
      - export FLASK_ENV=development
      - export FLASK_DEBUG=1 ,This will reduce need to restart server in case you make changes

5. On Your Browser You can try out a GET Method route like offices by appending the endpoint to
base localhost url such that it becomes
`127.0.0.1/api/v1/offices` and a json response will show
_`api/v1`_ comes from the defined blueprint      
6. For More Fine Grain Control Use Postman or Similar API Testing Service to use `POST`,`DELETE` AND `PATCH`
   using the below set of API endpoints collection \
   [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/945b3aaed258679b7a07)
7. For unit tests navigate to the tests folder and run `pytest` command in terminal
   If not installed check out the [documentation](https://docs.pytest.org/en/latest/getting-started.html)
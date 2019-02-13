# POLITICO-API
**POLITICO API** Is a pure Flask REST API app that serves endpoints for political parties,government offices,
petitioning,voting and user login and sign up to be consumed by front end frameworks.

!['PythonVersion''](https://img.shields.io/badge/python-3.6.7-yellow.svg)
!['License'](https://img.shields.io/badge/License-MIT-green.svg)
!['Travis'](https://travis-ci.org/Davidodari/POLITICO-API.svg?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3d4db0349f554fdfa87359e1eee2cd06)](https://app.codacy.com/app/Davidodari/POLITICO-API?utm_source=github.com&utm_medium=referral&utm_content=Davidodari/POLITICO-API&utm_campaign=Badge_Grade_Dashboard)
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
| /offices/<office_id>    |  DELETE  |  Deletes Specified Office  |
| /offices/<offices_id>   |  GET     |  Gets a specific office |
| /users                  |  POST    |  Adds User to List Of Users  |


## Author

[David Odari](https://github.com/Davidodari)

## Testing and Running Of App

##### Heroku

App Link Hosted On Heroku

[POLITICO-API on Heroku](https://blackpolitico-api-heroku.herokuapp.com/)

##### Local Machine

1. From your terminal clone The Repository on your machine \ it will be on develop branch
   `git clone https://github.com/Davidodari/POLITICO-API.git `

3. Start virtual env if is installed and created ,with python 3\ 
   `. venv/bin/activate` \
    to install the virtual env if missing use\
    ```pip3 install virtualenv```\
    and create virtual environment using the \
    ```python3 -m venv venv```
    
    Then Run The Above Commands to activate the virtual env when on the root folder of the project which will be
    Politico API

4. Install Flask in Virtual Environment    
    -  The terminal will be instatiate a virtual env and appear similar to what is shown below\
   ```(venv)blackcoder@blackPC:~/POLITICO-API$ ```
   -  Then Run \
    ```pip install -r requirements.txt``` \
    to download required packages for Flask
    
5. Run Flask App
   - Then run the following commands to set up the environment and config in the terminal
      - export FLASK_APP=run.py
      - export FLASK_ENV=development
      - export FLASK_DEBUG=1 ,This will reduce need to restart server in case you make changes
   - A link to where the app is hosted will appear in the terminal as shown in the below format
   ``` 
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```
   - With the above link apply a url prefix `/api/v1` such that its `http://127.0.0.1:5000/api/v1/endpoints`
   
5. Using an API Test Client like Postman or Insomnia you can run the above endpoints for each request.
   The Bodys of Requests are below\
   **Offices**
   ```
   {
   "name":"office_name",
   "type":"office_type"
   }
   ```
   **Parties**
   ```
   {
   "name":"party_name",
   "hqAddress":"party_address",
   "logoUrl":"party_logo"
   }
   ```
   As for update just use `name` key and value 
7. For unit tests  on the root folder run `pytest --cov api tests` command and tests will
   automatically be run with coverage 
   If not installed run the following command in terminal to install pytest with coverage in venv and run above  \
   ```pip install -U pytest-cov```
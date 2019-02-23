# POLITICO-API
**POLITICO API** Is a pure Flask REST API app that serves endpoints for political parties,government offices,
petitioning,voting and user login and sign up to be consumed by front end frameworks.

!['PythonVersion''](https://img.shields.io/badge/python-3.6.7-yellow.svg)
!['License'](https://img.shields.io/badge/License-MIT-green.svg)
!['Travis'](https://travis-ci.org/Davidodari/POLITICO-API.svg?branch=develop)
[![Coverage Status](https://coveralls.io/repos/github/Davidodari/POLITICO-API/badge.svg?branch=develop)](https://coveralls.io/github/Davidodari/POLITICO-API?branch=ch-refactor-tests-163807952)
[![Maintainability](https://api.codeclimate.com/v1/badges/4151dd7acdb2ddb19f1f/maintainability)](https://codeclimate.com/github/Davidodari/POLITICO-API/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/33734615352249b6823b104b386a6ea7)](https://www.codacy.com/app/Davidodari/POLITICO-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Davidodari/POLITICO-API&amp;utm_campaign=Badge_Grade)

### Endpoints  

####  Url Prefix - /api/v1/

<details>

 <summary> Version 1</summary>
 
|   ENDPOINT  | METHOD | STATUS |
|:---:|:---:|:---:|
| /offices                 |  GET     |  Gets List of offices |
| /offices                 |  POST    |  Adds an office to List of offices  |
| /parties                 |  GET     |  Gets List of Parties  |
| /parties                 |  POST    |  Adds a party to list of parties  |
| /parties/<party_id>      |  GET     |  Gets a specific party  |
| /parties/<party_id>/name |  PATCH   |  Updates Name value of a party  |
| /parties/<office_id>/name|  PATCH   |  Updates Office value of a office  |
| /parties/<party_id>      |  DELETE  |  Deletes Specified Party |
| /offices/<office_id>     |  DELETE  |  Deletes Specified Office  |
| /offices/<offices_id>    |  GET     |  Gets a specific office |
| /users                   |  POST    |  Adds User to List Of Users  |

</details>

####  Url Prefix - /api/v2/

<details>

 <summary> Version 2</summary>

|   ENDPOINT  | METHOD | STATUS |
|:---:|:---:|:---:|
| /offices                 |  GET     |  Gets List of offices |
| /offices                 |  POST    |  Adds an office to List of offices  |
| /parties                 |  GET     |  Gets List of Parties  |
| /parties                 |  POST    |  Adds a party to list of parties  |
| /parties/<party_id>      |  GET     |  Gets a specific party  |
| /parties/<party_id>/name |  PATCH   |  Updates Name value of a party  |
| /parties/<office_id>/name|  PATCH   |  Updates Office value of a office  |
| /parties/<party_id>      |  DELETE  |  Deletes Specified Party |
| /offices/<office_id>     |  DELETE  |  Deletes Specified Office  |
| /offices/<offices_id>    |  GET     |  Gets a specific office |
| /auth/signup             |  POST    |  Sign Up A User  |
| /auth/login              |  POST    |  Login  An Existing User  |
| /offices/<office_id>/register             |  POST    |  Sign Up A Candidate For An Office  |
| /offices/<office_id>/register             |  GET    |   Get A Candidate For A Specific Office  |
| /auth/login              |  POST    |  Login  An Existing User  |
| /votes/              |  POST    |  Users Can Vote  |
| /office/<office_id>/results              |  POST    |  Users Can Vote  |

</details>

## Author

[David Odari](https://github.com/Davidodari)

## Testing and Running Of App

##### Heroku

App Link Hosted On Heroku

[POLITICO-API on Heroku](https://blackpolitico-api-heroku.herokuapp.com/)

##### API Documentation

[POLITICO DOCS](https://politicoapi2.docs.apiary.io/#)

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
   <details>
   
   <summary> Models </summary>
   
   **Office**
   ```
   {
   "name":"office_name",
   "type":"office_type"
   }
   ```
   **Party**
   ```
   {
   "name":"party_name",
   "hqAddress":"party_address",
   "logoUrl":"party_logo"
   }
   ```
   **User**
   ```
   {
   "firstname":"first_name",
   "lastname":"last_name",
   "othername":"other_name",
   "email":"dedaap@them.mail.com",
   "phoneNumber":"+123442211",
   "password":"password"
   }
   ```
   </details>
   
   As for update just use `name` key and value on offices and parties 
7. For unit tests  on the root folder run `pytest --cov api tests` command and tests will
   automatically be run with coverage 
   If not installed run the following command in terminal to install pytest with coverage in venv and run above  \
   ```pip install -U pytest-cov```
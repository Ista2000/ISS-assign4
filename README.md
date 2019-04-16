# Intro to Software Systems Assignment 4
This repo is created for the assignment 4 of our course Introduction to Software Systems.

Deployed on heroku at https://shrouded-mountain-98925.herokuapp.com/

## To run it locally
- Run `git clone https://github.com/Ista2000/ISS-assign4.git` to clone this repository.
- Run `virtualenv env` to create a virtual environment for the project.
- Run `pip3 install -r requirements.txt` to install all the dependencies.
- Run `flask run` to run the app in your localhost.
- Visit `127.0.0.1:5000` for the website.

## API reference
- `/api/generate`
    - Arguments:
        - `sz`(Required): Size of the key
        - `e`(Optional): Set the e value, defaults to `0x1001`
    - Returns `n`, `e`, `p`, `q`, `d % (p-1)`, `d % (q-1)`, `coeff`, `d`  
- `/api/encrypt`
    - Arguments(All required):
        - `message`: The message to be encrypted
        -  `n`: The public key
        -  `e`: The exponent in the public key
    - Returns the encrypted message
- `/api/decrypt`
    - Arguments(All required):
        - `crypto`: The encrypted message
        - `n`: The private key
        - `d`: The `d` value in the private key
        - `e`: The exponent in the private key
        - `p`: The first prime in the private key
        - `q`: The second prime in the private key
    - Returns the decrypted message

## Util functions
- The functions all use the `rsa` python library which can be installed using `pip3 install rsa`
- All the util functions are written in `utils.py`
    - `generate(sz, e)`: returns `n`, `e`, `p`, `q`, `d % (p-1)`, `d % (q-1)`, `coeff`, `d` 
    - `encrypt(message, n, e)`: returns the encrypted message
    - `decrypt(crypto, n, d, e, p, q)`: returns the decrypted message

## Design patterns identified
- Factory pattern while initializing the database. An empty constructor is used to create an instant of the database object in the `models.py` file but the app context is added in `app.py`
- Singleton pattern while initializing the database. There cannot exist two different instants of the database object at some point of time, that is why a singleton pattern is alays used when initializing a database connection object

## Continuous integration
- Implemented continuous integration using TravisCI. The `.travis.yml` file is the config file used.
- Unit test cases written in `tests.py`

## Continuous Deployment
- A pipeline is set up in Heroku for continuous deployment. The link is given above. The `Procfile` file is the config file used.

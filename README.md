# Intro to Software Systems Assignment 4
This repo is created for the assignment 4 of our course Introduction to Software Systems.

Deployed on heroku at https://shrouded-mountain-98925.herokuapp.com/

All the functions used for the encryption and decryptions of text use APIs:
- `/api/generate`
    - Arguments:
        - `sz`(Required): Size of the key
        - `e`(Optional): Set the e value, defaults to `0x1001`
    - Returns `n`, `e`, `p`, `q`, `d % (p-1)`, `d % (q-1)`, `coeff`, `d`  
- `/api/encrypt`
    - Arguments(All required):
        - `message`: The message to be encrypted
        -  `n`
        -  `e`
    - Returns the encrypted message
- `/api/decrypt`
    - Arguments(All required):
        - `crypto`: The encrypted message
        - `n`
        - `d`
        - `e`
        - `p`
        - `q`

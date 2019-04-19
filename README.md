# Intro to Software Systems Assignment 4  <!-- omit in toc -->

## Abstract <!-- omit in toc -->

- As part of this assignment we ported experiment PKCS_v1.5 of Cryptography lab which is written with PHP as backend to Flask with MVC.
- Used OOPS-Concepts (Classes) to add *Database* functionality for storing Feedback entered & also the responses of Quizzes. [Routes for retreiving Data from Database](#routes-for-retreiving-data-from-database)
- Implemented *API* for experiment and made calls to it from Javascript, this ensures end users cannot see the logic behind the experiment which was previously written in Javascript. ([API reference](#api-reference))
- Used [Design & Architectural Patterns](#design--architecural-patterns-used).
- Created unit test cases & implemented [Continuous Integration](#continuous-integration) using Travis
- Used Heroku for [Continuous Deployment](#continuous-deployment)
- Created External Documentation (this file - README.md)


Deployed on heroku at https://shrouded-mountain-98925.herokuapp.com/

> **Note** : In case of $\LaTeX$ not rendering properly (i.e, showing \$'s), install extension for browser to enable $\LaTeX$ on github markdown. (Eg: For Chrome - [this](https://chrome.google.com/webstore/detail/tex-all-the-things/cbimabofgmfdkicghcadidpemeenbffn/related?hl=en))


# Table of Contents <!-- omit in toc -->
- [To run it locally](#to-run-it-locally)
- [Theory of Experiment](#theory-of-experiment)
  - [Key generation](#key-generation)
  - [Key syntax](#key-syntax)
    - [Public-key syntax](#public-key-syntax)
    - [Private-key syntax](#private-key-syntax)
  - [Encryption process](#encryption-process)
    - [Encryption-block formatting](#encryption-block-formatting)
    - [Octet-string-to-integer conversion](#octet-string-to-integer-conversion)
    - [RSA computation](#rsa-computation)
    - [Integer-to-octet-string conversion](#integer-to-octet-string-conversion)
  - [Decryption process](#decryption-process)
    - [Octet-string-to-integer conversion](#octet-string-to-integer-conversion-1)
    - [RSA computation](#rsa-computation-1)
    - [Integer-to-octet-string conversion](#integer-to-octet-string-conversion-1)
    - [Encryption-block parsing](#encryption-block-parsing)
- [API reference](#api-reference)
- [Util functions](#util-functions)
- [Design & Architecural patterns Used](#design--architecural-patterns-used)
- [Continuous integration](#continuous-integration)
- [Continuous Deployment](#continuous-deployment)
- [Routes for retreiving Data from Database](#routes-for-retreiving-data-from-database)

## To run it locally
- Run `git clone https://github.com/Ista2000/ISS-assign4.git` to clone this repository and `cd` into it.
- Run `virtualenv env` to create a virtual environment for the project.
- Run `source env/bin/activate` from root of repo to activate virtual enviornment
- Run `pip3 install -r requirements.txt` to install all the dependencies.
- Run `python3 -m flask run` to run the app in your localhost.
- Visit `127.0.0.1:5000`* for the website.     
  \*might differ if port busy


## Theory of Experiment

### Key generation

Each entity shall select a positive integer e as its public exponent.

Each entity shall privately and randomly select two distinct odd
primes p and q such that (p-1) and e have no common divisors, and
(q-1) and e have no common divisors.

The public modulus n shall be the product of the private prime
factors p and q:

$$n = pq$$

The private exponent shall be a positive integer d such that de-1 is
divisible by both p-1 and q-1.

### Key syntax

#### Public-key syntax

An RSA public key shall have ASN.1 type RSAPublicKey:

RSAPublicKey ::= SEQUENCE {
   modulus INTEGER, -- n
   publicExponent INTEGER -- e }

The fields of type RSAPublicKey have the following meanings:

+ modulus is the modulus n.
+ publicExponent is the public exponent e.

#### Private-key syntax

An RSA private key shall have ASN.1 type RSAPrivateKey:

RSAPrivateKey ::= SEQUENCE {
   version Version,
   modulus INTEGER, -- n
   publicExponent INTEGER, -- e
   privateExponent INTEGER, -- d
   prime1 INTEGER, -- p
   prime2 INTEGER, -- q
   exponent1 INTEGER, -- d mod (p-1)
   exponent2 INTEGER, -- d mod (q-1)
   coefficient INTEGER -- (inverse of q) mod p }

The fields of type RSAPrivateKey have the following meanings:

+ version is the version number, for compatibility with future revisions of this document. It shall be 0 for this version of the document.
+ modulus is the modulus n.
+ publicExponent is the public exponent e.
+ privateExponent is the private exponent d.
+ prime1 is the prime factor p of n.
+ prime2 is the prime factor q of n.
+ exponent1 is d mod (p-1).
+ exponent2 is d mod (q-1).
+ coefficient is the Chinese Remainder Theorem
      coefficient q-1 mod p.

### Encryption process

The encryption process consists of four steps: encryption- block
formatting, octet-string-to-integer conversion, RSA computation, and
integer-to-octet-string conversion. The input to the encryption
process shall be an octet string D, the data; an integer n, the
modulus; and an integer c, the exponent. For a public-key operation,
the integer c shall be an entity's public exponent e; for a private-
key operation, it shall be an entity's private exponent d. The output
from the encryption process shall be an octet string ED, the
encrypted data.

The length of the data D shall not be more than k-11 octets, which is
positive since the length k of the modulus is at least 12 octets.
This limitation guarantees that the length of the padding string PS
is at least eight octets, which is a security condition

#### Encryption-block formatting

A block type BT, a padding string PS, and the data D shall be
formatted into an octet string EB, the encryption block.

EB = 00 || BT || PS || 00 || D            
Equation (1)

The block type BT shall be a single octet indicating the structure of
the encryption block. For this version of the document it shall have
value 00, 01, or 02. For a private- key operation, the block type
shall be 00 or 01. For a public-key operation, it shall be 02.

The padding string PS shall consist of k-3-||D|| octets. For block
type 00, the octets shall have value 00; for block type 01, they
shall have value FF; and for block type 02, they shall be
pseudorandomly generated and nonzero. This makes the length of the
encryption block EB equal to k.

#### Octet-string-to-integer conversion

The encryption block EB shall be converted to an integer x, the
integer encryption block. Let EB1, ..., EBk be the octets of EB from
first to last. Then the integer x shall satisfy

$$x = \Sigma_{i=1}^{k} 2^{8(k-i)}\ EBi$$  
Equation (2)

In other words, the first octet of EB has the most significance in
the integer and the last octet of EB has the least significance.

Note. The integer encryption block x satisfies $0 \le x <  n$ since EB1
= 00 and $2^{(8(k-1))} \le  n$.

#### RSA computation

The integer encryption block x shall be raised to the power c modulo
n to give an integer y, the integer encrypted data.

$$y = x^c \bmod n \ ,\ \ 0 \le y < n$$

This is the classic RSA computation.

#### Integer-to-octet-string conversion

The integer encrypted data y shall be converted to an octet string ED
of length k, the encrypted data. The encrypted data ED shall satisfy

$$y = \Sigma_{i=1}^{k} 2^{8(k-i)}\ EDi$$  
Equation (3)

where ED1, ..., EDk are the octets of ED from first to last.

In other words, the first octet of ED has the most significance in
the integer and the last octet of ED has the least significance.


### Decryption process

The decryption process consists of four steps: octet-string-to-
integer conversion, RSA computation, integer-to-octet-string
conversion, and encryption-block parsing. The input to the decryption
process shall be an octet string ED, the encrypted data; an integer
n, the modulus; and an integer c, the exponent. For a public-key
operation, the integer c shall be an entity's public exponent e; for
a private-key operation, it shall be an entity's private exponent d.
The output from the decryption process shall be an octet string D,
the data.

It is an error if the length of the encrypted data ED is not k.

For brevity, the decryption process is described in terms of the
encryption process.

#### Octet-string-to-integer conversion

The encrypted data ED shall be converted to an integer y, the integer
encrypted data, according to Equation (3).

It is an error if the integer encrypted data y does not satisfy $0 \le
y < n$.

#### RSA computation

The integer encrypted data y shall be raised to the power c modulo n
to give an integer x, the integer encryption block.

$$x = y^c \bmod n \ ,\ \ 0 \le x < n$$

This is the classic RSA computation.

#### Integer-to-octet-string conversion

The integer encryption block x shall be converted to an octet string
EB of length k, the encryption block, according to Equation (2).

#### Encryption-block parsing

The encryption block EB shall be parsed into a block type BT, a
padding string PS, and the data D according to Equation (1).

It is an error if any of the following conditions occurs:

+ The encryption block EB cannot be parsed unambiguously (see notes to Section 8.).
+ The padding string PS consists of fewer than eight octets, or is inconsistent with the block type BT.
+ The decryption process is a public-key operation and the block type BT is not 00 or 01, or the decryption process is a private-key operation and the block type is not 02.


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


## Design & Architecural patterns Used

- Factory pattern while initializing the database. An empty constructor is used to create an instant of the database object in the `models.py` file but the app context is added in `app.py`
- Singleton pattern while initializing the database. There cannot exist two different instants of the database object at some point of time, that is why a singleton pattern is alays used when initializing a database connection object


## Continuous integration

- Implemented continuous integration using TravisCI. The `.travis.yml` file is the config file used.
- Unit test cases written in `tests.py`


## Continuous Deployment

- A pipeline is set up in Heroku for continuous deployment. The link is given above. The `Procfile` file is the config file used.


## Routes for retreiving Data from Database

- Visit route `/see-all-feedback` to view all the feedbacks entered by users
- Visit route `/see-all-quizzes` to view all the responses entered by users in quizzes 

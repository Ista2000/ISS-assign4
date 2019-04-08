import pytest
import random
import string

# Add parent folder to path
# import sys 
# sys.path.append('..')

# # # Import rsa file
# # from utils.py import *
# # # import utils.py

# import sys, os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

from utils import *

# import rsa


# def generate(sz, e=None):
#     if e:
#         public_key, private_key = rsa.newkeys(sz, exponent=e)
#     else:
#         public_key, private_key = rsa.newkeys(sz)

#     return hex(private_key.n), public_key.e, hex(private_key.exp1 * private_key.exp2), hex(private_key.p), \
#         hex(private_key.q), hex(private_key.d % (private_key.p - 1)), hex(private_key.d % (private_key.q - 1)), \
#         hex(private_key.coef), public_key, private_key


# def encrypt(message, n, e):
#     public_key = rsa.PublicKey(n, e)
#     return rsa.encrypt(str.encode(message), public_key)


# def decrypt(crypto, n, e, d, p, q):
#     private_key = rsa.PrivateKey(n, e, d, p, q)
#     return rsa.decrypt(crypto, private_key)



# Number of test cases to run
num_tests = 10

def randomString(stringLength):
    """Generate a random string of given length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def testing512():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(512)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"

def testing1024():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(1024)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"

def testing3_512():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(512, 3)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"


def testing3_1024():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(1024, 3)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"
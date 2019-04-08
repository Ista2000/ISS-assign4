import rsa


def generate(sz, e=None):
    if e:
        public_key, private_key = rsa.newkeys(sz, exponent=e)
    else:
        public_key, private_key = rsa.newkeys(sz)

    return hex(private_key.n), public_key.e, hex(private_key.exp1 * private_key.exp2), hex(private_key.p), \
        hex(private_key.q), hex(private_key.d % (private_key.p - 1)), hex(private_key.d % (private_key.q - 1)), \
        hex(private_key.coef), public_key, private_key


def encrypt(message, n, e):
    print(str.encode(message), n, e)
    public_key = rsa.PublicKey(n, e)
    return rsa.encrypt(str.encode(message), public_key)


def decrypt(crypto, n, e, d, p, q):
    private_key = rsa.PrivateKey(n, e, d, p, q)
    return rsa.decrypt(crypto, private_key)

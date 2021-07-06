from math import gcd 
import random


# we set the number in range to save time
min_size = 1
max_size = 200

def fast_exponentiation_power2(x, y, z):
    # fast exponentiation for x^y mod z
    ex = 1
    res = (x ** ex) % z
    while (ex < y):
        res = (res * res) % z
        ex *= 2
    return res

def fermat_test(n):
    isPrime = True
    a = random.randint(1, n)
    # we assume 10 attempts at the fermat test is enough
    for _ in range(10):
        result = fast_exponentiation_power2(a, (n-1), n)
        if (result != 1):
            isPrime = False
            break
        else:
            a = random.randint(1, n)
    return isPrime

def prime_generator():
    p = random.randint(min_size, max_size)
    while True:
        if (fermat_test(p)):
            return p
        else:
            p = random.randint(min_size, max_size)

def safe_prime_generator():
    p = random.randint(min_size, max_size)
    while True:
        if (fermat_test(p)):
            if fermat_test((p-1)/2):
                return p
            else:
                p = random.randint(min_size, max_size)

def generate_e(phi_n):
    e = random.randint(1, phi_n)
    while True:
        if (gcd(e, phi_n) == 1):
            return e
        else:
            e = random.randint(1, phi_n)

def generate_d(e, phi_n):
    i = 1
    d = ((phi_n * i) + 1) / e
    while not d.is_integer():
        d = ((phi_n * i) + 1) / e
        i += 1
    return d
        
def RSA_encrypt(m, d, n):
    return (m ** d) % n

def RSA_decrypt(c, e, n):
    return (c ** e) % n

def RSA():
    # generate p and q
    p = prime_generator()
    q = prime_generator()
    while (q == p):
        q = prime_generator()

    n = p * q
    phi_n = (p-1) * (q-1)
    e = generate_e(phi_n)
    d = generate_d(e, phi_n)

    return (e, n), (d, n)

# Testing part
# obtain private and public keys:
k_pub, k_priv = RSA()

m1 = 3
m2 = 5

# encrypt both using public key
c1 = RSA_encrypt(m1, k_pub[0], k_pub[1])
c2 = RSA_encrypt(m2, k_pub[0], k_pub[1])

m1_new = RSA_decrypt(c1, k_priv[0], k_priv[1])

# result in plaintext space:
res_plain = m1 * m2
add_plain = m1 + m2

# since RSA is partially homomorphic, we can perform multiplication in the cipher space as well
# and we will get the same result

# result in cipher space:
mult_cipher = c1 * c2
res_cipher = RSA_decrypt(mult_cipher, k_pub[0], k_pub[1])
add_cipher = c1 + c2
res_cipher1 = RSA_decrypt(add_cipher, k_pub[0], k_pub[1])
print(k_pub)
print(k_priv)
print(f"plaintext multiplication: {res_plain}")
print(f"ciphertext multiplication: {res_cipher}")

print(f"plaintext addition: {add_plain}")
print(f"ciphertext addition: {add_cipher}")

# rsa-phe
Proof that RSA encryption is partially homomorphic

Has some minor bugs on occasion, such as "OverflowError: (34, 'Result too large')", when max float value is exceeded, could be fixed by decimal module for example.
Example output:

(37, 85) #public key
(45.0, 85) #private key
plaintext multiplication: 15
ciphertext multiplication: 15
plaintext addition: 8
ciphertext addition: 138

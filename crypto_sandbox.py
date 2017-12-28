import time
from binascii import unhexlify, hexlify
import operator
from math import gcd
from random import randint
from useful import modinv, is_prime, totient, primes, next_prime
import numbthy
import factorize


start = time.time()

# print(next_prime(7676634861344985432)*next_prime(13298400830464428876)*next_prime(76766348261344543321))


print(factorize.factorize(7836843693546096609372307891785217547112922821466006851143, True))

elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)
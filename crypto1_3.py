# SHA-256 hash of a movie file, done in a streamable way

import time
from binascii import hexlify
from Crypto.Hash import SHA256


start = time.time()

with open('6.1.intro.mp4_download', 'rb') as f:
    full = []
    while True:
        raw = f.read(1024)
        if not raw:
            break
        full.insert(0, raw)

h = bytes()
for block in full:
    hash_input = block + h
    h = SHA256.new(hash_input).digest()

print(hexlify(h).decode())

elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)
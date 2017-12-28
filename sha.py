# SHA hash

import time
from Crypto.Hash import SHA256
from binascii import hexlify


start = time.time()

h = SHA256.new()

with open('Test.pdf', 'rb') as f:
    raw = True
    while raw:
        raw = f.read(102400)
        h.update(raw)

print(h.hexdigest())

elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)
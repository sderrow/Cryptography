# AES in CBC and CTR modes

import time
import Crypto.Cipher.AES as AES
import operator
from binascii import unhexlify


def decode_cbc(key, ct):
    cipher = AES.new(unhexlify(key))
    ct = unhexlify(ct)
    bs = cipher.block_size

    m = bytes()
    for i in range(bs, len(ct), bs):
        input1 = ct[i-bs:i]
        input2 = cipher.decrypt(ct[i:i+bs])
        p = bytes(map(operator.xor, input1, input2))
        m += p
    pad = m[-1]
    m = m[:-pad]
    return m.decode()


def decode_ctr(key, ct):
    cipher = AES.new(unhexlify(key))
    ct = unhexlify(ct)
    bs = cipher.block_size

    iv = bytearray(ct[:bs])
    m = bytes()
    for i in range(bs, len(ct), bs):
        input1 = ct[i:i+bs]
        input2 = cipher.encrypt(bytes(iv))
        iv[-1] += 1
        p = bytes(map(operator.xor, input1, input2))
        m += p
    return m.decode()

start = time.time()

k1 = '140b41b22a29beb4061bda66b6747e14'
ct1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
ct2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
print(decode_cbc(k1, ct1))
print(decode_cbc(k1, ct2))

k2 = '36f18357be4dbd77f050515c73fcf9f2'
ct3 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
ct4 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
print(decode_ctr(k2, ct3))
print(decode_ctr(k2, ct4))


elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)
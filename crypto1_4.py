# Padding oracle attack on a website

import time
import urllib.request
import urllib.error
from binascii import unhexlify, hexlify
from operator import xor


class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib.request.quote(q)  # Create query URL
        try:
            f = urllib.request.urlopen(target)        # Wait for response
        except urllib.error.HTTPError as e:
            # print("We got: {}".format(e.code))     # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

start = time.time()

TARGET = 'http://crypto-class.appspot.com/po?er='
po = PaddingOracle()

a = 'etaoinsrhldcumfpgwybvkxjqz'
common_bytes = [ord(c) for c in ' .,'] + [ord(c) for c in a] + [ord(c) - 32 for c in a] + [ord(c) for c in '0123456789:;'] + [ord("'"), ord('"')]
common_bytes += [i for i in range(256) if i not in common_bytes]

ct = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
ct_b = unhexlify(ct)

bs = 16
block_count = len(ct_b) // bs
pt = bytearray(len(ct_b) - bs)
flag = False

for i in range(block_count, 1, -1):
    original = ct_b[:bs*i]
    p1 = bytearray(len(original))
    for position in range(1, bs+1):
        if p1[-bs-position] > 0:
            continue
        p2 = bytearray(len(original))
        for j in range(1, position + 1):
            p2[-bs-j] = position
        for proposal in common_bytes:
            p1[-bs-position] = proposal
            candidate = bytes(map(xor, original, map(xor, p1, p2)))
            rl = hexlify(candidate).decode()
            if po.query(rl):
                if not flag:
                    flag = True
                    for k in range(1, proposal + 1):
                        pt[-k] = proposal
                        p1[-bs-k] = proposal
                print('Block {:d}, position {:d} = {:d} --> {}'.format(i-1, position, proposal, chr(proposal)))
                pt[bs*(i-1)-position] = proposal
                break

pt = pt[:-pt[-1]]
print(pt.decode())

elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)
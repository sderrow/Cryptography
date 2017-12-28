# Discrete log

import time
from useful import modinv


def dlog(h, g, p):
    B = 2 ** 20
    A = pow(g, B, p)
    tab1 = {}
    g_inv = modinv(g, p)
    lhs = h

    for x1 in range(B + 1):
        tab1[lhs] = x1
        lhs = lhs * g_inv % p

    rhs = 1
    for x0 in range(B + 1):
        try:
            x1 = tab1[rhs]
            return (x0 * B + x1) % p
        except KeyError:
            pass
        rhs = rhs * A % p
    raise Exception('Discrete log not found')

start = time.time()

p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

x = dlog(h, g, p)
print(x)
# print("Check = {}".format(h == pow(g, x, p)))

elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)
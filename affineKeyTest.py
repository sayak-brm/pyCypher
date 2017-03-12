# This program proves that the keyspace of the affine cipher is limited
# to len(SYMBOLS) ^ 2.

import affineCipher, cryptomath

message = input('Enter Message:')
for keyA in range(2, 100):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))

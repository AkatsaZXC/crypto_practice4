"""
1. Choose two prime numbers p and q.
   2. Compute n = p*q.
   3. Calculate phi = (p-1) * (q-1).
   4. Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1; i.e., e and phi(n) are coprime.
   5. Calculate d as d ≡ e−1 (mod phi(n)); here, d is the modular multiplicative inverse of e modulo phi(n).
   6. For encryption, c = me mod n, where m = original message.
   7. For decryption, m = c d mod n.
"""
from math import fmod


def gcd(a, b):
    while True:
        t = a % b
        if t == 0:
            return b
        a = b
        b = t


def calculation():
    p = 3
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 7

    while e < phi:
        track = gcd(e, phi)
        if track == 1:
            break
        else:
            e += 1
    d1 = 1 / e
    d = fmod(d1, phi)
    message = [5, 9, 15]
    for i in message:
        c = pow(i, e)
        m = pow(c, d)
        c = fmod(c, n)
        m = fmod(m, n)
        print("Обычное сообщение: ", i)
        print("Зашифрованние сообщение: ", c)
        print("Расшифрованное сообщение: ", round(m))


def main():
    calculation()


if __name__ == '__main__':
    main()

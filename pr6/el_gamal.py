import random
from math import pow

a = random.randint(2, 10)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


#  Генерация больших рандомных чисел
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key


#  Модульное возведение в степень
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c


#  Асимметричное шифрование
def encrypt(msg, q, h, g):
    en_message = []

    k = gen_key(q)  # Приватный ключ для отправителя
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_message.append(msg[i])

    print("g^k использован : ", p)
    print("g^ak использован : ", s)
    for i in range(0, len(en_message)):
        en_message[i] = s * ord(en_message[i])

    return en_message, p


#  Дешифрование

def decrypt(en_message, p, key, q):
    dr_message = []
    h = power(p, key, q)
    for i in range(0, len(en_message)):
        dr_message.append(chr(int(en_message[i] / h)))

    return dr_message


def main():
    message = 'filippov'
    print(f"Обычное сообщение: {message}")

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    key = gen_key(q)  # Приватный ключ для получателя
    h = power(g, key, q)
    print("g использован : ", g)
    print("g^a использован : ", h)

    en_message, p = encrypt(message, q, h, g)
    dr_message = decrypt(en_message, p, key, q)
    decrypted_message = ''.join(dr_message)
    print(f"Расшифрованное сообщение: {decrypted_message}")


if __name__ == '__main__':
    main()

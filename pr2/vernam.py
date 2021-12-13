from random import randint
from re import findall

crypt_mode = input("[E]ncrypt|[D]ecrypt: ").upper()
if crypt_mode not in ['E', 'D']:
    print("Error: режим не найден")
    raise SystemExit

message = input("Введите сообщение: ").upper()


def regular(text):
    return findall(r"[0-9]+", text)


def encrypt_decrypt(mode, message, final="", keys=[]):
    if mode == 'E':
        for symbol in message:
            key = randint(0, 25);
            keys.append(str(key))
            final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
        return final, '.'.join(keys)
    else:
        keys = input("Введите ключи: ")
        for index, symbol in enumerate(message):
            final += chr((ord(symbol) - int(regular(keys)[index]) - 13) % 26 + ord('A'))
        return final


print("Итоговое сообщение: ", encrypt_decrypt(crypt_mode, message))

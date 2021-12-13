crypt_mode = input("[E]ncrypt|[D]ecrypt: ").upper()
if crypt_mode not in ['E', 'D']:
    print("Error: режим не найден")
    raise SystemExit

message = input("Введите сообщение: ").upper()
one_key = input("Введите ключ: ").upper()


def encrypt_decrypt(mode, message, key, final=""):
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + ord(key[index])
        else:
            temp = ord(symbol) - ord(key[index])
        final += chr(temp % 26 + ord('A'))
    return final


print("Итоговое сообщение: ", encrypt_decrypt(crypt_mode, message, one_key))

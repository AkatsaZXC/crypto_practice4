crypt_mode = input("[E]ncrypt|[D]ecrypt: ").upper()
if crypt_mode not in ['E', 'D']:
    print("Error: режим не найден")
    raise SystemExit
message = input("Введите строку для шифрования: ").upper()
try:
    rot_key = int(input("Введите ключ: "))
except ValueError:
    print("Error: ключ должен быть int")
    raise SystemExit


def encrypt_decrypt(mode, message, key, final=""):
    for symbol in message:
        if mode == 'E':
            final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
        else:
            final += chr((ord(symbol) - key - 13) % 26 + ord('A'))
    return final


print("Итоговое сообщение: ", encrypt_decrypt(crypt_mode, message, rot_key))


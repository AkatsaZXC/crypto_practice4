message = input("Введите сообщение: ").upper()
alphabet_default = [chr(x) for x in range(65, 91)]  # по таблице ASCII
alphabet_reverse = list(alphabet_default)
alphabet_reverse.reverse()
final = ""

for symbol in message:
    for index_alphabet, symbol_alphabet in enumerate(alphabet_default):
        if symbol == symbol_alphabet:
            final += alphabet_reverse[index_alphabet]
print("Итоговое сообщение: ", final)

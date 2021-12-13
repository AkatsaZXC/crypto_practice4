def encryption():
    print("Исходный алфавит: ")
    #  Заполнения алфвавита из строки и проверка на длину каждой строки
    alphabet_list = []
    alphabet_str = "АБВГДЕЁЖЗИйКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-*#"
    for s in alphabet_str:
        alphabet_list.append(s)
    k = 0
    for s in alphabet_list:
        print(f"|{s}|", end=' ')
        k = k + 1
        if k == 6:
            print("\n")
            k = 0
    print()

    key_fraze = input("Введите ключевую фразу: ").upper()
    print("Ключевая фраза: ")
    print(key_fraze)
    print()
    key_fraze_list = list(key_fraze)

    #  Удаление лишних элементов из ключевой фразы
    sorted_key_fraze = list()
    for s in key_fraze_list:
        if s not in sorted_key_fraze:
            sorted_key_fraze.append(s)
    #  Дополнение элементами сортированного ключ.слова алфвавита
    for index, symbol in enumerate(sorted_key_fraze):
        alphabet_list.insert(index, symbol)

    #  Удаление всех повторяющихся элементов из списка
    new_alphabet_list = list()
    for s in alphabet_list:
        if s not in new_alphabet_list:
            new_alphabet_list.append(s)
    #  Вывод нового алфвавита
    print("Новый алфавит: \n")
    k = 0
    for s in new_alphabet_list:
        print(f"|{s}|", end=' ')
        k = k + 1
        if k == 6:
            print("\n")
            k = 0
    print()

    #  Запрос на фразу для шифрования
    str_to_encrypt = input("Введите строку для шифрования: ").upper()
    str_to_encrypt_list = list(str_to_encrypt)
    print("Ваша строка: ")
    print(str_to_encrypt)

    # Замена букв в слове на символ в алфвавите + 6 шагов
    indexes_list = list()
    for s in str_to_encrypt_list:
        if s in new_alphabet_list:
            indexes_list.append(new_alphabet_list.index(s))
    output_fraze = list()
    for i in indexes_list:
        if i >= 30:
            output_fraze.append(new_alphabet_list[i - 30])
        else:
            output_fraze.append(new_alphabet_list[i + 6])

    # Вывод итоговой фразы
    print("Зашифрованная фраза: ")
    for s in output_fraze:
        print(s, end='')
    print()


def main():
    encryption()


if __name__ == '__main__':
    main()
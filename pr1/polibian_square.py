def encryption():
    square_list = [['*', 1, 2, 3, 4, 5, 6],
                   [1, 'А', 'Б', 'В', 'Г', 'Д', 'Е'],
                   [2, 'Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                   [3, 'Л', 'М', 'Н', 'О', 'П', 'Р'],
                   [4, 'С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                   [5, 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                   [6, 'Э', 'Ю', 'Я', '.', '!', '-'],
                   ]
    print("Исходный квадрат: ")
    print()

    #  Вывод квадрата в консоль
    for i in range(len(square_list)):
        for j in range(len(square_list[i])):
            print(square_list[i][j], end=' ')
        print()

    print("Желаете заполнить квадрат своим алфавитом?[Y/N]")
    result = input()
    result = result.upper()

    if result == 'Y':
        alphabet_str = input("Введите алфавит:\n")
        #  Отрезать часть строки, если она больше 36
        if len(alphabet_str) < 36:
            print("Введите не менее 36 символов")
            exit()
        alphabet_str = alphabet_str[:36].upper()
        alphabet_list = list(alphabet_str)
        print("Ваш алфавит:")
        for s in alphabet_list:
            print(f"{s}", end='')
        print()

        #  Создание словаря со значениями для шифрования
        alphabet_dict = {}
        values = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51,
                  52,
                  53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
        values = list(map(str, values))
        #  Заполнение словаря значениями из values и ключами из alphabet_list
        i = 0
        for i, k in enumerate(alphabet_list):
            alphabet_dict[k] = values[i]
        print()

        fraze = input("Введите фразу для шифрования:\n")
        fraze = fraze.upper()

        #  Кодирование сообщения по значению по ключу из словаря
        def decoder(fraze):
            new_fraze = ""
            #  list_fraze = list(def_fraze)
            for x in fraze:
                if x in alphabet_dict:
                    new_fraze += alphabet_dict[x]
                else:
                    new_fraze += x
            return new_fraze

        output = decoder(fraze)
        print(output)

    elif result == 'N':
        alphabet_list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
                         'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', '!', '-']

        print("Ваш алфавит:")
        for s in alphabet_list:
            print(f"{s}", end='')
        print()

        #  Создание словаря со значениями для шифрования
        alphabet_dict = {}
        values = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51,
                  52,
                  53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
        values = list(map(str, values))
        #  Заполнение словаря значениями из values и ключами из alphabet_list
        i = 0
        for i, k in enumerate(alphabet_list):
            alphabet_dict[k] = values[i]
        print()

        fraze = input("Введите фразу для шифрования:\n")
        fraze = fraze.upper()

        #  Кодирование сообщения по значению по ключу из словаря
        def decoder(fraze):
            new_fraze = ""
            #  list_fraze = list(def_fraze)
            for x in fraze:
                if x in alphabet_dict:
                    new_fraze += alphabet_dict[x]
                else:
                    new_fraze += x
            return new_fraze

        output = decoder(fraze)
        print(output)
    else:
        print('Выход')
        exit()


def main():
    encryption()


if __name__ == '__main__':
    main()
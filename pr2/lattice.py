from random import choice, randint

squade = 10
alphabet_list = [chr(x) for x in range(65, 91)] + [chr(y) for y in range(97, 123)]
string_list = [choice(alphabet_list) for _ in range(squade * squade)]


def get_key(text):
    while True:
        keys = [randint(0, 99) for _ in range(len(text))]
        for number in keys:
            switch = False
            if keys.count(number) > 1:
                switch = True
                break
            if not switch:
                return keys


def lattice(index=0):
    print(end=' ')
    for string in range(squade):
        print(string, end=' ')
    for string in range(squade):
        print()
        for column in range(squade):
            if index % squade == 0:
                print(index // squade, end='|')
            print(string_list[index], end='|')
            index += 1
    print()


message = input("Введите сообщение: ")
key_list = get_key(message)
key_list.sort()
print("Ключи: ", key_list)
for index, symbol in enumerate(message):
    del string_list[key_list[index]]
    string_list.insert(key_list[index], symbol)
lattice()
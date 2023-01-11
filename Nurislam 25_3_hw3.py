# дз на 11.11.2022


while True:

    word = input('Введите слово :').lower()
    if word == 'Выход'.lower():
        print("Программа завершена !")
        break
    d = len(word)
    print('Количество букв:', d)
    glasnye = 0
    soglasnye = 0

    for i in range(0, len(word)):
        if word[i] == 'а' or word[i] == 'i' or word[i] == 'u' or word[i] == 'o' or word[i] == 'e':
            glasnye = glasnye + 1
        elif word[i] == 'а' or word[i] == 'я' or word[i] == 'у' or word[i] == 'ю' \
                or word[i] == 'о' or word[i] == 'е' or word[i] == 'и' or word[i] == 'ё' or word[i] == 'э' \
                or word[i] == 'ы':
            glasnye += 1
        else:
            soglasnye += 1

    print('Количество гласных :', glasnye)
    print('Количестов согласныых :', soglasnye)
    print(f"гласные/согласные:{round(glasnye / len(word) * 100, 2)}%/{round(soglasnye / len(word) * 100,2)}%\n")

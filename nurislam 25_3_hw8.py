# дз №8


number = input("Введите загаданное вами число в диапазоне [0;100]: ")
start = 1
finish = 100
c = 0
numbers = []
while True:

    current_numbers = (start + finish)//2
    is_numbers = input('Ваше число:{}?\n( , <, >)\n'.format(current_numbers))    # пробел = обозначает да!!!
    numbers.append(current_numbers)
    c += 1
    if is_numbers.lower() == ' ' :
        print(' PC WINS!''\nGAME OVER!')
        break
    elif is_numbers =='<':
        start = current_numbers + 1
    elif is_numbers == '>':
        finish = current_numbers - 1
    else:
        print("Неправильнй ввод! Допустимые символы: '<', '>' и ' '")

    with open('result.txt', 'w', encoding='UTF-8') as file:
        file.write(f'Количество попыток-{c}\nСписок попыток-{numbers}\nЗагаданное число-{current_numbers}')









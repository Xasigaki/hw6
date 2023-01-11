# def func(word):
#     if type(word) != str:
#         return False
#     return word.split()[0]
#
#
# print(func('Hello world!'))

#
# def average_number(*args):
#     return sum(args) / len(args)
#
#
# print(round(average_number(23, 25, 75, 81, 32, 99)), 1)
#
#
# def password_is_good(word):
#     has_digit = 0
#     has_low_let = 0
#     has_up_let = 0
#     for i in word:
#         if i.isdigit():
#             has_digit += 1
#         if i.isalpha():
#             if i.islower():
#                 has_low_let += 1
#             else:
#                 has_up_let += 1
#     return len(word) >= 6 and has_digit and has_low_let and has_up_let
#
#
# print('Введите пароль: ')
# word = input('-> ')
# if password_is_good(word):
#     print('Пароль надежный.')
# else:
#     print('Пароль ненадежный!')

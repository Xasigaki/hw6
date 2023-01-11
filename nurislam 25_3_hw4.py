# дз 15,11,2022


data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = [i for i in data_tuple if type(i) not in [int, float, bool]]
numbers = [i for i in data_tuple if type(i) != str]

del numbers[:1]
deleted = numbers.pop(0)

letters.append(deleted)
numbers.insert(1, 2)

numbers.reverse()
letters.reverse()

letters[1] = 'G'
letters[7] = 'c'

numbers[1] = 4
numbers[2] = 9

print(tuple(letters))
print(tuple(numbers))
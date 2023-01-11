# ДЗ №7

ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2==0, ten))
evens1 = list(map(lambda x: x**2, evens))
# print(evens)
# print(evens1)

def function(ind=ten):
    while True:
        print(ten)
        index = input("Введите индекс:").lower()
        if index == 'выход' or index == "exit":
            print('Выход успешно выполнен!')
            break
        try:
            print(ind[int(index)])
        except:
            print('Tакого индекса не сушествует!')

function()











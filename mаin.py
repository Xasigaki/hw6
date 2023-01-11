import colorama
import math,datetime

# MRO

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def __str__(self):
    #     return f'меня зовут {self.name} и мне {self.age} лет'

hum=Human('Бекболот',21)
hum.age=45
# print(hum)

class Human2(Human):
    def __init__(self,name,age,nasa=False):
        super().__init__(name,age)
        self.nasa=nasa
    # def _n(self):
    #     self.nasa=True
    # def t(self):
    #     self.age *= 2
    def __orientation(self):
        print(f'{self.name} скрывает свою ориентацию')
    def year(self):
        print(f'{2023-self.age}')

    def car(self):
        print(f'{self.name} водит машину с 18 лет, его стаж вождения {self.age - 18}')

    def emka(self):
        print(f'Имя: {self.name}')

    def dancho_bratan(self):
        print(f'Возраст: {self.age}')

    def wh(self):
        while True:
            Human2.aldik(self)



    def aldik(self):
        print(f'1-возраст\n'
              f'2-имя\n'
              f'3-дата рождения\n'
              f'4-машина\n'
              f'5-ориентация\n'
              f'6-выход')
        a = int(input('Введите число: '))
        if a == 1:
            Human2.emka(self)
        elif a == 2:
            Human2.dancho_bratan(self)
        elif a == 3:
            Human2.year(self)
        elif a == 4:
            Human2.car(self)
        elif a == 5:
            Human2.__orientation(self)
        elif a == 6:
            exit()



    def count_methods(self):
        print(len(dir(self)))




w = Human2('Mirdjalalydin', 23)
w.count_methods()

w.wh()
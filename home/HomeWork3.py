"""ДЗ - 3"""


class Bank:
    money = 'money'
    people = 'people'

    def __init__(self,name='Speedwagon',balance=100022032):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f'{self._name}\n' \
               f'{self._balance}\n'
    def moneyX(self):
        amount = int(input('Сколько добавить?'))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _plus(self, obj):
        return self._balance + obj._balance
c = Bank()
b = Bank()
b.moneyX()
# b._kill()
print(b)
print(b._plus(c))

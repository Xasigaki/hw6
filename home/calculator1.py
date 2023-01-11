class Calculator:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __truediv__(self, other):
        return self.val / other.val

a = Calculator(int(input('число №1:')))
b = Calculator(int(input('число №2:')))

"""если надо что б работал только один знак
ТОГДА УБЕРИТЕ ОСТАЛЬНЫЕ ПРИНТЫ!!!!!!!!"""
# тоесть ненужные принты просто закоментируйте


print(a + b)
print(a - b)
print(a * b)
print(a / b)










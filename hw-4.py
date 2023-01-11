class First:
    def __init__(self, name):
        self.name = name

class Second:
    def __init__(self, age):
        self.age = age

class Third(First):
    def n(self):
        print('жашоо збс')


class Fourth(Second):
    def a(self):
        print('ахеуть')


class Fifth(Third,Fourth):

    def __init__(self, name, age):
        First.__init__(self, name)
        Second.__init__(self, age)

    def __str__(self):
        return f' {self.name} {self.age}'

f = Fifth('xs',12)
# f = Fifth(12)
f.n()
f.a()
print(f)





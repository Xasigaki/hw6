class Hero:
    name = 'name'
    abyliti = 'abyliti'
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class Hero_super(Hero):

    def __init__(self, name, abyliti):
        Hero.__init__(self, name, abyliti)

    def __str__(self):
        return f'is it superhero - {self.name}\n'\
               f'abyliti -> {self.abyliti}'




a = Hero_super('Jotaro Kujo','STAR PLATINUM')
b = Hero_super('Dio Brando', 'ZAWAARUDO')

print(a)
print(b)
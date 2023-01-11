"""ДЗ №1"""

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_hp(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return f'name is->{self.name}\n'\
               f'nickname is ->{self.nickname}\n' \
               f'superpower is ->{self.superpower}\n' \
               f'have ->{self.health_points} hp'

    def __len__(self):
        return len(self.catchphrase)


hero2 = SuperHero('Joseph Jostar', 'JoJo', 'hamon', 10001, 'и следушее твое слово будет ...')

hero2.double_hp()
hero2.catchphrase

print(hero2)


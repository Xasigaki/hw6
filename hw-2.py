# 07.12.2022


class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points  = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def n(self):
        print(f'It was me: {self.name}')

    def h(self):
        self.health_points *= 2

    def __str__(self):
        return f'Nickname: {self.nickname}\n' \
               f'Power: {self.superpower}\n' \
               f'Health: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Arthur Boyle', 'knight king', 'igniting sword', 105, 'The King of Knights, fused with his steed, is invulnerable!')
hero.n()
hero.h()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}\n')

# доч. 1класс
class Air_hero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        shinrah = self.health_points ** 2
        self.health_points = shinrah

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase\n')

shinra = Air_hero('Shinra Kusakabe','devil','Adolla burst', 199, "If something happens again, call. After all, that's what heroes are for, after all.")
shinra.h()
print(shinra)
print(f'Damage: {shinra.damage}')
shinra.f()
print(f'Fly: {shinra.fly}')
shinra.phrase()


# доч. 2класс
class Hero_destroyer(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        Benymaru = self.health_points ** 2
        self.health_points = Benymaru

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase\n')

Benymaru = Hero_destroyer('Benymaru Shinmon', 'King of destruction Asakus', 'Kagetsu', 280, 'I will bring destruction')
Benymaru.h()
print(Benymaru)
print(f'Damage: {Benymaru.damage}')
Benymaru.f()
print(f'Fly: {Benymaru.fly}')
Benymaru.phrase()

# доч. класс от нового класса
class Villain(Hero_destroyer):
    monster = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self):...

    def crit(self):
        print(f'Crit dm: {self ** 2}')


Burns = Villain(':Leonard', 'white lion', 'dupelganger', 300, 'let there be power')
print(Burns)
Burns.gen_x()
Villain.crit(Benymaru.damage)
import random


class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} выполняет шаг вперед")

    def attack(self):
        print(f"{self.name} наносит атаку")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows <= 0:
            print(f"{self.name} закончились стрелы, не может атаковать")
            return
        self.arrows -= 1
        if random.random() < self.precision:
            print(f"{self.name} попал!")
        else:
            print(f"{self.name} промахнулся!")

    def rest(self):
        self.arrows += 0
        print(f"{self.name} восстановил стрелы.Готов для чтобы начать атаку!")

    def status(self):
        return f"Имя:{self.name}, Hp: {self.hp}, Arrows: {self.arrows}, Pre: {self.precision}"


hero = Archer("Asitaka", 100, 5, 100)

hero.action()
hero.attack()
# hero.attack()
# hero.attack()
# hero.attack()
# hero.attack()
# hero.attack()
hero.attack()
hero.rest()
hero.status()

print(hero.status())

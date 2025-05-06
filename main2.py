# Верблюжая натация
# Змеиная натация

# WarriorHero
# warrior_hero

# Наследование


# Родительский , Супер класс

# class Person:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return print(f"Я {self.name},мой уровень {self.lvl}, у меня столько хп {self.hp}")

    def action(self):
        return print(f'{self.name} выполняет базовое действие!!')


hero = Hero("samat", 100, 100)


#
# # Дочерний класс
# # элипс ... выполняет ту же функцию что pass
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return print(f"Кастую огонь")
#
#     def action(self):
#         return print(f"{self.name} ничего не делает")
#
#
# mage_hero = MageHero("samat", 100, 100, 100)
#
# mage_hero.action()
#
# mage_hero.cast_spell()

class Animal:
    def action(self):
        return print("Animal action")


class Swim:
    def action(self):
        return print("Swim action")

class Fly:

    def action(self):
        return print("Fly action")


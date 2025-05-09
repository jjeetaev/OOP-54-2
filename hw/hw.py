class Person:
    def __init__(self, name="John Doe", age=18, city="Bishkek"):
        self.name_1 = name
        self.age_1 = age
        self.city_1 = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name_1}, мне {self.age_1} лет, я живу в городе {self.city_1}")

    def is_adult(self):
        return self.age_1 >= 18


# person1 = Person("Temirlan", 18, "Bishkek")
# person2 = Person(age=18, name="Samat", city="Bishkek")
#
# person1.introduce()
# person2.introduce()

person1 = Person("Temirlan", 18, "Bishkek")
person2 = Person("Samat", 16, )
person3 = Person("Atai", 19, "Bishkek")

print(f"{person1.age_1} лет, {person1.is_adult()}" )
print(f"{person2.age_1} лет, {person2.is_adult()}" )
print(f"{person3.age_1} лет, {person3.is_adult()}" )

class Person:
    def __init__(self, name, age, city):
        self.name_1 = name
        self.age_1 = age
        self.city_1 = city

    def introduce(self):
        print(f"Привет,меня зовут {self.name_1}, мне {self.age_1} , мой город {self.city_1}")


fullname = Person("Temirlan", 18, "Bishkek")

fullname.introduce()

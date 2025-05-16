from faker import Faker

fake = Faker()

name = fake.name()
address = fake.address()
email = fake.email()

print("Фейковое имя:", name)
print("Фейковый адрес:", address)
print("Фейковый email:", email)

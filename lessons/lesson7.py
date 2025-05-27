import sqlite3

# Альбом из А4
connect = sqlite3.connect("users.db")

# Рука ручка
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')


connect.commit()


def add_user(name: str, age: int, hobby="None"):
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?,?,?)",
        (name, age, hobby)
    )
    print(f"{name} - Добавлен")


# add_user('Josh',26, "Спать")
# connect.commit()



def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)

    for i in users:
        print(f"NAME:{i[0]} AGE: {i[1]}, HOBBY{i[2]}")

# get_all_users()


def update_user(name, rowid):
    cursor.execute('UPDATE users SET name = ? WHERE rowid = ?',
    (name, rowid)
    )
    connect.commit()
    print("Обновление произошло!")

# update_user('Kyle',1)



# def delete_user(rowid):
#     cursor.execute(
#         'DELETE FROM users WHERE rowid = ?',
#         (rowid,)
#     )
#     connect.commit()
#
# delete_user(3)

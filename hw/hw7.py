import sqlite3

# Альбом из А4
connect = sqlite3.connect("users.db")

# Рука ручка
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    hobby TEXT DEFAULT 'None',
    user_id INTEGER
)
''')

connect.commit()


def add_user(name: str, age: int, hobby="None", user_id=None):
    cursor.execute(
        "INSERT INTO users(name, age, hobby, user_id) VALUES (?, ?, ?, ?)",
        (name, age, hobby, user_id)
    )
    connect.commit()
    print(f"{name} - Добавлен c user_id {user_id}")


add_user('Josh', 26, "Спать", 1)
add_user('Josh', 22, "Спать", 2)
add_user('Josh', 19, "Спать", 3)

connect.commit()


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


connect = sqlite3.connect("users.db")
cursor = connect.cursor()


def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        user_dict = {
            "id": user[0],
            "name": user[1],
            "age": user[2],
        }
        return user_dict
    else:
        print("Пользователь не найден.")
        return None


if __name__ == "__main__":

    uid = int(input("Введите ID пользователя: "))
    result = get_user_by_id(uid)
    if result:
        print("Найден пользователь:", result)

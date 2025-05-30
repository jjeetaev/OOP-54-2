import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

# Создание таблиц
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR(100) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')
connect.commit()


# Функция добавления пользователя
def add_user(name: str, age: int, hobby="None"):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")


# Функция добавления оценки
def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()
    print("Оценка за урок добавлена!!")


# Функция получения пользователей и их оценок
def get_user_and_grades():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.user_id = grades.userid
    ''')

    users = cursor.fetchall()

    for row in users:
        name = row[0]
        subject = row[1] if row[1] is not None else "Нет предмета"
        grade = row[2] if row[2] is not None else "Нет оценки"
        print(f"NAME: {name}, SUBJECT: {subject}, GRADE: {grade}")


# get_user_and_grades()

def create_view_most_diverse_users():
    cursor.execute("DROP VIEW IF EXISTS view_most_diverse_users")

    cursor.execute('''
        CREATE VIEW view_most_diverse_users AS
        SELECT u.user_id, u.name, COUNT(DISTINCT g.subject) AS subject_count
        FROM users u
        JOIN grades g ON u.user_id = g.userid
        GROUP BY u.user_id
        HAVING subject_count = (
            SELECT MAX(subjects_per_user)
            FROM (
                SELECT COUNT(DISTINCT subject) AS subjects_per_user
                FROM grades
                GROUP BY userid
            )
        )
    ''')
    connect.commit()
    print("Представление 'view_most_diverse_users' создано!")


def show_most_diverse_users():
    cursor.execute("SELECT * FROM view_most_diverse_users")
    rows = cursor.fetchall()
    print("\nПользователи с наибольшим количеством разных предметов:")
    for row in rows:
        user_id, name, subject_count = row
        print(f"ID: {user_id}, NAME: {name}, SUBJECTS: {subject_count}")
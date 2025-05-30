import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

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
        subject VARCAHR(100) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')
connect.commit()


def add_user(name: str, age: int, hobby="None"):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")


# add_user("John", 26, "Спать")
# add_user("John2", 26, "Спать")
# add_user("John3", 26, "Спать")
# add_user("John4", 26, "Спать")


def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()

    print("Оценка за урок добавлена!!")


# add_grade(1, "Математика", 5)
# add_grade(1, "Физика", 3)
# add_grade(1, "ИЗО", 2)
# add_grade(1, "Физра", 4)
# add_grade(10, "Химия", 3)

def get_user_and_grades():
    try:
        cursor.execute('''
            SELECT users.name, grades.subject, grades.grade
            FROM users 
            LEFT JOIN grades ON users.user_id = grades.userid
            ORDER BY users.name, grades.subject
        ''')
        users = cursor.fetchall()

        if not users:
            print("В базе данных нет информации о пользователях и оценках")
            return

        print("\nСписок пользователей и их оценок:")
        current_user = None
        for user in users:
            name, subject, grade = user
            if name != current_user:
                print(f"\n{name}:")
                current_user = name
            if subject:  # Проверяем что subject не None
                print(f"  {subject}: {grade}")
            else:
                print("  Нет оценок")

    except sqlite3.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")


connect = sqlite3.connect("users.db")
cursor = connect.cursor()
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


# Функция для добавления пользователей
def add_user(name: str, age: int, hobby="None"):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")


# Функция для добавления оценок
def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()
    print("Оценка за урок добавлена!!")


# 1. Представление с пользователями, у которых средняя оценка выше 4.5
def create_view_top_students():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS top_students AS
    SELECT u.user_id, u.name, AVG(g.grade) as avg_grade
    FROM users u
    JOIN grades g ON u.user_id = g.userid
    GROUP BY u.user_id, u.name
    HAVING avg_grade > 4.5
    ORDER BY avg_grade DESC
    ''')
    connect.commit()
    print("Представление top_students создано")


def show_top_students():
    cursor.execute('SELECT * FROM top_students')
    print("\nТоп студенты (средний балл > 4.5):")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Имя: {row[1]}, Средний балл: {row[2]:.2f}")


# 2. Представление с пользователями, их хобби и количеством предметов
def create_view_users_hobbies_subjects():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS users_hobbies_subjects AS
    SELECT 
        u.user_id, 
        u.name, 
        u.hobby,
        COUNT(DISTINCT g.subject) as subjects_count
    FROM users u
    LEFT JOIN grades g ON u.user_id = g.userid
    GROUP BY u.user_id, u.name, u.hobby
    ''')
    connect.commit()
    print("Представление users_hobbies_subjects создано")


def show_users_hobbies_subjects():
    cursor.execute('SELECT * FROM users_hobbies_subjects')
    print("\nПользователи с хобби и количеством предметов:")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Имя: {row[1]}, Хобби: {row[2]}, Предметов: {row[3]}")


# 3. Представление с самыми "разносторонними" пользователями
def create_view_versatile_users():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS versatile_users AS
    SELECT 
        u.user_id, 
        u.name,
        COUNT(DISTINCT g.subject) as different_subjects
    FROM users u
    JOIN grades g ON u.user_id = g.userid
    GROUP BY u.user_id, u.name
    ORDER BY different_subjects DESC
    LIMIT 5
    ''')
    connect.commit()
    print("Представление versatile_users создано")


def show_versatile_users():
    cursor.execute('SELECT * FROM versatile_users')
    print("\nСамые разносторонние пользователи:")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Имя: {row[1]}, Разных предметов: {row[2]}")


# Исправленная функция для получения пользователей и их оценок
def get_user_and_grades():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users LEFT JOIN grades ON users.user_id = grades.userid
    ''')
    users = cursor.fetchall()
    print("\nВсе пользователи и их оценки:")
    for i in users:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")


# Основная функция для демонстрации
def main():
    # Добавляем тестовые данные
    add_user("John", 26, "Спать")
    add_user("Alice", 24, "Рисование")
    add_user("Bob", 25, "Программирование")
    add_user("Eva", 23, "Музыка")

    add_grade(1, "Математика", 5)
    add_grade(1, "Физика", 4)
    add_grade(2, "Математика", 5)
    add_grade(2, "Литература", 5)
    add_grade(3, "Математика", 4)
    add_grade(3, "Физика", 4)
    add_grade(3, "Химия", 5)
    add_grade(4, "Математика", 5)
    add_grade(4, "Физика", 5)
    add_grade(4, "Химия", 5)
    add_grade(4, "Биология", 5)



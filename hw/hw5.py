# 1
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("is_admin"):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")

    return wrapper


@require_admin
def delete_user(user):
    print(f"User {user['name']} deleted")


delete_user({"name": "temirlan", "is_admin": True})
delete_user({"name": "samat", "is_admin": False})


# 2


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершена")
        return result

    return wrapper


@logger
def say_hello():
    print("Hello!")


say_hello()

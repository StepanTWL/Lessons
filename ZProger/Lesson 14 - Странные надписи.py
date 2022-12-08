import random

a = [2]
b, = a
print(b)  # 2


def get_values() -> list:
    return [random.randint(0, 9) for _ in range(20)]


user_id, user_foto, *values = get_values()
print(user_id)

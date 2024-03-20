from string import ascii_uppercase, ascii_lowercase, digits
from random import sample

IN_FILE_NAME = "scientist.txt"  # Имя входного файла
OUT_FILE_NAME = "scientist_password.csv"  # Имя выходного файла


def create_login_by_name(name):
    """Функция, которая переводит полное ФИО человека в его логин

    :return: str
    """

    second_name, first_name, treed_name = name.split()
    return f"{second_name}_{first_name[0]}{treed_name[0]}"


def create_password():
    """Функция, которая генерирует пароль

    :return: str
    """

    while True:
        password = "".join(
            sample(ascii_uppercase + ascii_lowercase + digits, 10)
        )

        # Проверка, что пароль действительно соответствует требованиям
        if (
            len(set(password) & set(ascii_uppercase)) and
            len(set(password) & set(ascii_lowercase)) and
            len(set(password) & set(digits))
        ):
            return password


with open(IN_FILE_NAME, encoding="utf8") as in_file:
    title, *lines = [elem.rstrip().split("#") for elem in in_file.readlines()]

# Добавляем новые столбцы
title.extend(["login", "password"])
for index in range(len(lines)):
    lines[index].extend(
        [
            create_login_by_name(lines[index][0]),
            create_password(),
        ],
    )

with open(OUT_FILE_NAME, "w", encoding="utf8", newline="") as out_file:
    print(*title, sep="#", file=out_file)
    for row in lines:
        print(*row, sep="#", file=out_file)

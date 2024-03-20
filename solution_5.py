from random import sample

IN_FILE_NAME = "scientist.txt"  # Имя входного файла
OUT_FILE_NAME = "scientist_with_hash.csv"  # Имя выходного файла


def create_hash(string):
    """Функция, которая генерирует хэш

    :return: str
    """

    a_1 = sample(range(0, 1024), 1024)
    lst = []
    for elem in string:
        i = ord(elem) % 1024
        lst.append(a_1[i])
    res = sum(lst) % 2048

    return res


with open(IN_FILE_NAME, encoding="utf8") as in_file:
    title, *lines = [elem.rstrip().split("#") for elem in in_file.readlines()]


# Добавляем новые столбцы
title = ["hash"] + title
for index in range(len(lines)):
    lines[index] = [create_hash(lines[index][0])] + lines[index]


with open(OUT_FILE_NAME, "w", encoding="utf8", newline="") as out_file:
    print(*title, sep="#", file=out_file)
    for row in lines:
        print(*row, sep="#", file=out_file)
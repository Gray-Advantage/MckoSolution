from datetime import datetime

IN_FILE_NAME = "scientist.txt"

with open(IN_FILE_NAME, encoding="utf8") as in_file:
    title, *lines = [elem.rstrip().split("#") for elem in in_file.readlines()]

lines.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))


def get_date_input(string):
    """Функция, которая переводит строку в формат datetime %d.%m.%Y,
    если ввод некорректен, то вернёт None

    :return: datetime
    """

    try:
        return datetime.strptime(string, "%d.%m.%Y")
    except ValueError:
        return None


def get_initials(name):
    """Функция, которая переводит полное ФИО человека в его инициалы

    :return: str
    """

    second_name, first_name, treed_name = name.split()
    return f"{second_name} {first_name[0]}.{treed_name[0]}."


print("Введите дату в формате `ДД.ММ.ГГГГ`")
print("Для выхода введите слово `эксперимент`", end="\n\n")
res = input(">>> ")
while res != "эксперимент":
    date = get_date_input(res)

    if date is None:
        print("Ввод некорректен! Введите дату в формате `ДД.ММ.ГГГГ`")
    else:
        empty_print = True

        for row in lines:
            row_date = datetime.strptime(row[2], "%Y-%m-%d")
            if row_date == date:
                empty_print = False
                print(
                    f"Ученый {get_initials(row[0])} создал препарат: "
                    f"{row[1]} - {row_date.strftime('%d.%m.%Y')}"
                )

        if empty_print:
            print("В этот день ученые отдыхали")

    res = input(">>> ")

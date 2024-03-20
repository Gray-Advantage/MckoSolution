from datetime import datetime

IN_FILE_NAME = "scientist.txt"
OUT_FILE_NAME = "scientist_origin.txt"

with open(IN_FILE_NAME, encoding="utf8") as in_file:
    title, *lines = [elem.rstrip().split("#") for elem in in_file.readlines()]

lines.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))


# Поиск подельников препарата Аллопуринол
allopunol_rows = []
for row in lines:
    if row[1] == "Аллопуринол":
        allopunol_rows.append(row)

print("Разработчиками Аллопуринола были такие люди:")
print()
print(*[f"{elem[0]} - {elem[2]}" for elem in allopunol_rows][1:], sep="\n")
print()
print("Оригинальный рецепт принадлежит:", allopunol_rows[0][0])

# Очистка от ученых злоумышленников
new_lines = []
for row in lines:
    if row[1] not in [elem[1] for elem in new_lines]:
        new_lines.append(row)

with open(OUT_FILE_NAME, "w", encoding="utf8", newline="") as out_file:
    print(*title, sep="#", file=out_file)
    for row in new_lines:
        print(*row, sep="#", file=out_file)

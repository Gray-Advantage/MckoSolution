from datetime import datetime

IN_FILE_NAME = "scientist.txt"

with open(IN_FILE_NAME, encoding="utf8") as in_file:
    title, *lines = [elem.rstrip().split("#") for elem in in_file.readlines()]

lines.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))

print(*[f"{elem[0]}: {elem[1]}" for elem in lines][:5], sep="\n")

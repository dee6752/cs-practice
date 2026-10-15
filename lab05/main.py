import os
from tablestats import read_rows, count_types, total_minutes, to_csv
def main():
    filename = input().strip()
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден")
        return
    with open(filename, encoding="utf-8") as table:
        lines = table.readlines()
    rows = read_rows(lines)
    print(len(rows))
    counts = count_types(zrows)
    print(len(counts))
    error_minutes = total_minutes(rows, "ошибка")
    print(error_minutes)
    summary_text = to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(summary_text)
if __name__ == "__main__":
    main()

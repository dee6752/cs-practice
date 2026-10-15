import os
from tablestats import read_rows, count_types, total_minutes, to_csv

def main():
    # Читаем имя таблицы из первой строки ввода
    filename = input().strip()
    
    # Проверяем существование файла (хорошая практика)
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден")
        return

    # Читаем и обрабатываем данные
    with open(filename, encoding="utf-8") as table:
        lines = table.readlines()
        
    rows = read_rows(lines)
    
    # 1. Сколько записей прочитано
    print(len(rows))
    
    # 2. Сколько различных типов
    counts = count_types(rows)
    print(len(counts))
    
    # 3. Суммарные минуты записей типа "ошибка"
    error_minutes = total_minutes(rows, "ошибка")
    print(error_minutes)
    
    # Запись сводки в summary.csv
    summary_text = to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(summary_text)

if __name__ == "__main__":
    main()
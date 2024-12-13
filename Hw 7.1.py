def read_last(lines, file):
    # Проверка, что lines - положительное целое число
    if not isinstance(lines, int) or lines <= 0:
        print("Ошибка: количество строк должно быть положительным целым числом.")
        return

    try:
        with open(file, 'r', encoding='utf-8') as f:
            # Считываем все строки файла
            all_lines = f.readlines()
            
            # Если количество строк больше, чем в файле, выводим все строки
            if lines >= len(all_lines):
                print("Файл содержит меньше строк, чем запрашиваемое количество.")
                for line in all_lines:
                    print(line.strip())
            else:
                # Выводим последние 'lines' строк
                for line in all_lines[-lines:]:
                    print(line.strip())

    except FileNotFoundError:
        print(f"Ошибка: файл '{file}' не найден.")

read_last(3, 'C:/Users/Moonlight/Desktop/article.txt')
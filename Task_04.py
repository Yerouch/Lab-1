month = input("Введите месяц (по-русски со строчной буквы в Им.п.): ")
if month == 'январь' or month == 'март' or month == 'май' or month == 'июль' or month == 'август' or month == 'октябрь' or month == 'декабрь':
    print("В данном месяце 31 день.")
elif month == 'апрель' or month == 'июнь' or month == 'сентябрь' or month == 'ноябрь':
    print("В данном месяце 30 дней.")
elif month == 'февраль':
    print("В данном месяце 28 или 29 дней.")
else:
    print("В названии месяца ошибка.")

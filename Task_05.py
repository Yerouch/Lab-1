coordinates = input("Введите координаты клетки: ")
if (int(coordinates[1]) % 2) != 0:
    if coordinates[0] == 'a' or coordinates[0] == 'c' or coordinates[0] == 'e' or coordinates[0] == 'g':
        print("Клетка чёрная.")
    else:
        print("Клетка белая.")
else:
    if coordinates[0] == 'a' or coordinates[0] == 'c' or coordinates[0] == 'e' or coordinates[0] == 'g':
        print("Клетка белая.")
    else:
        print("Клетка чёрная.")

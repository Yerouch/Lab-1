human_age = int(input("Введите возраст человека: "))
if human_age > 21:
    dog_age = 2 + (human_age-21)/4
    print("Аналогичный возраст собаки:", dog_age)
elif human_age < 0:
    print("Ошибка: отрицательный возраст")
else:
    dog_age = human_age/10.5
    print("Аналогичный возраст собаки:", dog_age)

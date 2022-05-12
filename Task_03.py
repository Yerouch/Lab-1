letter = input("Введите строчную латинскую букву: ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("Буква гласная.")
elif letter == 'y':
    print("Буква может быть как гласной, так и согласной.")
else:
    print("Буква согласная.")

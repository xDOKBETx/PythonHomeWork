day = int(input("Введите число: "))
if day == 6 or day == 7:
    print("Да")
elif 1 <= day <= 5:
    print("Нет")
else:
    print('Некорректный ввод. Попробуйте снова')

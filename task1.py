day_num = int(input("Введите день недели:"))

if day_num == 1:
    print("Понедельник")
elif day_num == 2:
    print("Вторник")
elif day_num == 3:
    print("Среда")
elif day_num == 4:
    print("Четверг")
elif day_num == 5:
    print("Пятница")
elif day_num > 5 and day_num < 8:
    print("Выходной")
else:
    day_num > 7
    print("В неделе всего семь дней!!!")
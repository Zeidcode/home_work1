x = int(input("Введите координаты x :"))
y = int(input("Введите координаты y :"))

 
if x > 0 and y > 0:
    print("Точка в I координатной четверти")
if x < 0 and y > 0:
    print("Точка во II координатной четверти")
if x < 0 and y < 0:
    print("Точка в III координатной четверти")
if x > 0 and y < 0:
    print("Точка в IV координатной четверти")
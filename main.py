x = float(input("Введите x ")) #инициализируем переменную x и просим ввести ее значение.
y = float(input("Введите y ")) #инициализируем переменную y и просим ввести ее значение.
if x == 0 and y == 0: #вводим условие при котором оба значения равны нулю
    print("точка расположена в середине координат") #выводим если значения равны нулю
elif x == 0 and y != 0: #вводим условие
    print("точка расположена на плоскости x") #выводим если значения равны 0 и не нулю
elif y == 0 and x != 0: #вводим условие
    print("точка расположена на плоскости y") #выводим если значения равны нулю и не нулю
elif y < 0 and x < 0: #вводим условие
    print("точка находится в 3 четверти") #выводим если оба значения меньеш нуля
elif y < 0 and x > 0: #вводим условие
    print("точка находится в 4 четверти") #выводим если одно значение меньше нуля а другое больше
elif y > 0 and x < 0: #вводим условие
    print("точка находится в 2 четверти") #выводим если одно значение меньше нуля а другое больше 
elif y > 0 and x > 0: #вводим условие
    print("точка находится в 1 четверти") #выводим если оба значения больше нуля       
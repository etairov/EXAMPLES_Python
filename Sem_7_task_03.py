# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
#--------------------------------------

def same_by(characteristic, objects):
    for i in range(len(objects) - 1):
        if characteristic(objects[i]) != characteristic(objects[i + 1]):
            return False
    return True

values = [1.1, 2.1, 10.1, 6.1]
if same_by(lambda x: isinstance(x, float), values): #проверка на инт
    print('same')
else:
    print('different')
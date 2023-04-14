# Хакер Василий получил доступ к классному журналу
# и хочет заменить все минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные на минимальные.
# Ввод: 5 --> 1 3 3 3 4
# Вывод:  1 3 3 3 1
#----------------------------

from random import randint
n = int(input("Введите кол-во оценок в журнале: "))
list1 = [randint(1, 5) for _ in range(n)] # метод list comprehension или генератор списка
print(list1)
max_mark = max(list1)
min_mark = min(list1)
for i in range(n):
    if list1[i] == max_mark:
        list1[i] = min_mark
print(list1)

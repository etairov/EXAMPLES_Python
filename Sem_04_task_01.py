# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# --------------------------------------------

list = input('Введите строку: ').split()
dict = {}
print(list)
for i in list:
    if i not in dict:
        dict.update({i: 0})
    else:
        dict[i] += 1
    if dict[i] != 0:
        print(f'{i}_{dict[i]}', end=' ')
    else:
        print(f'{i}', end=' ')

# -----------------------------------------
print()
# Через метод get

sp = input("Введите строку: ").split()
result = {}
for i in sp:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1

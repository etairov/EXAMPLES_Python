# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
#-------------------------------------------

from random import randint

list = []
n = 10
for i in range(n):
    list.append(randint(-10, 10))
print(list)
print(len(set(list)))
#-------------------------------

list = []
n = 10
temp = 0
for i in range(n):
    list.append(randint(-10, 10))
print('-------------------------------------')
print(f'{list}- random')

for i in range(0, len(list)):
    for j in range(0, len(list) - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(f'{list}- sorted')

unrepeat = 0
for i in range(0, len(list)):
    if list[i - 1] != list[i]:
       unrepeat += 1
print(f'Кол-во различных чисел {unrepeat}')

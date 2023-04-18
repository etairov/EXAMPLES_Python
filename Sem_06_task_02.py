# Задача №39
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве.
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# -----------------------------------

from random import randint as rnd

n = int(input("Введите кол-во элементов в 1-м списке: "))
list = [rnd(1, 10) for _ in range(n)]
print(list)
cnt = 0

for i in range(1, len(list) - 1):
    if list[i - 1] < list[i] and list[i + 1] < list[i]:
        cnt += 1

print(cnt)

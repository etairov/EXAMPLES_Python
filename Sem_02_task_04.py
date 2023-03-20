# Задача No15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9

from random import randint

n = int(input("Введите кол-во арбузов: "))
count = 0
print(f'{n} ->', end=" ")
mass = [randint(5, 15) for i in range(n)]
print(mass, end=" ")

max_ = min_ = mass[0]
for i in range(0, n):
    if mass[i] > max_:
        max_ = mass[i]

    elif mass[i] < min_:
        min_ = mass[i]
        i += 1
print(f' Min= {min_} Max= {max_}')






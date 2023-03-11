#Задача No5. Решение в группах
#Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
#а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
#В каждом вагоне написан его номер.
#Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
#Он хочет определить, сколько всего вагонов в электричке.
#Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
#Input: 3 4(ввод на разных строках)
#Output: 6
#----------------------------------------------

print("Введите номер вагона с начала поезда: ")
c1 = int(input())
print("Введите номер вагона по билету: ")
c2 = int(input())

if c1 > c2 or c1 < c2:
    w = c2 + (c1 - 1)
    print(f'Кол-во вагонов в поезде {w}')

elif c1 == c2:
    print(f'Необходима дополнительная информация')


#За день машина проезжает n километров.
#Сколько дней нужно, чтобы проехать маршрут длиной m километров?
#При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700 m = 750 Output: 2
#-------------------------------------------
import math

print("Введите дневной пробег: ")
n = int(input())
print("Введите пробег всего маршрута: ")
m = int(input())
d = math.ceil(m/n)
print(f'Машина пройдет маршрут за {d} дней')
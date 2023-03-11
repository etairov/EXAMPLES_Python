#Определить наибольшее число из двух введенных чисел.
#--------------------------------------------------

print("Enter the number (a): ")
a = input()
print("Enter the number (b) ")
b = input()
if a > b:
    print(f'{a} > {b}')
elif a == b:
    print(f'{a} = {b}')
else:
    print(f'{b} > {a}')
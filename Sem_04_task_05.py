# перемешать список заданыый произвольно. [2,5,7,8] to [2,7,5,8]
# ---------------------------------------------------------------
from random import shuffle

x = [[i] for i in range(4)]
print(x)
shuffle(x)
print(x)


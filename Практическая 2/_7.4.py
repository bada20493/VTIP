import math
import random
def Igra(x):
    N=random.randint(1,10)
    if N==x:
        print('Победа!!')
    else:
        print('Попробуйте еще раз')
print('Введите число от 1 до 10')
x=int(input())
Igra(x)
    

import math
def F(x):
    if (x>=0.2) and (x<=0.9):
        print('Значение функции = ',round(math.sin(x),3))
    else :
        print('Значение функции = 1')
x=float(input('Введите x = '))
F(x)

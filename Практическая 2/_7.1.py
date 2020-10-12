import math
def Ger(a,b,c):
    p=(a+b+c)/2 
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Площадь треугольника равна : ',round(S,3))
print('Введите стороны реугольника')
a,b,c=map(int,input().split())
Ger(a,b,c)

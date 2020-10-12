import math
def Sin(x):
    V=math.sqrt(1-math.sin(x)**2)
    print('Выражение равно : ',round(V,3))
print('Введите x')
x=int(input())
Sin(x)

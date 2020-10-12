import math
def vr(x,y):
    z=(x+(2+y)/x**2)/(y+1/(math.sqrt(x**2+10)))
    q=2.8*math.sin(x)+math.fabs(y)
    print('Значение z = '+str(round(z,3))+'\n Значение q = ',round(q,3))
x=int(input('Введите x = '))
y=int(input('Введите y = '))
vr(x,y)

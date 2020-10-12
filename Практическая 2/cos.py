import math
def Cos(x):
    n=2
    m=1
    cos=x
    while(round(abs(m),4)>0.001):
        m=(-1**(n-1))*(x**(2*n-2))/(math.factorial(2*n-2))
        cos=round(cos,4)+round(m,4)
        n=n+1
    return(cos)

x=float(input("Введите x: "))
print(Cos(x))

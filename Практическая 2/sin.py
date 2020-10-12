import math
def Sin(x):
    n=2
    m=1
    sin=x
    while(round(abs(m),4)>0.001):
        m=(-1**(n-1))*(x**(2*n-1))/(math.factorial(2*n-1))
        sin=round(sin,4)+round(m,4)
        n=n+1
    return(sin)

x=float(input("Введите x: "))
print(Sin(x))

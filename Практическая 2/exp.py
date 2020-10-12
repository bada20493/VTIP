import math
def Exp(x):
    n=1
    exp=1
    m=1
    while(m>0.0001):
        m=(x**n)/(math.factorial(n))
        n=n+1
        exp=exp+round(m,4)
    return(exp)

x=int(input("Ведите степень е: "))
print(Exp(x))

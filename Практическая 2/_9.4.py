L = [3, 'hello','привет', 7, 4,  4, 3, -1]
def Strok(L):
    if 'привет' in L :
        L.remove('привет')
        print(L)
    else :
        L.append('Hello')
        print(L)
def St(L):
    k = 0
    for i in range(len(L)):
        if L[i]==4:
            k=k+1
    if k>1:
        L.clear()
        print(L)
Strok(L)
St(L)


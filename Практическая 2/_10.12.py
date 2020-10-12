import random
N = int(input('Введите количество строк :'))
M = int(input('Введите количество столбцов :'))
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random.randint(1,10)*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print()
kol=0
num=0
for i in range(M-1): 
    for j in range(N-1):
        kol_new=a[i].count(a[i][j])
        if kol_new>kol:
            kol=kol_new 
            num=i
print('Строка с максимальным количеством одинаковых элементов : ',num+1)

#1
def Sum(L):
    if sum(L): print(len(L))
def MM(L):
    p=max(L)-min(L)
    if p>10: print(sorted(L))
    else:print('Разность меньше 10')
L = [3, 6, 7, 4, -5, 4, 3, -1]
Sum(L)
#2
MM(L)

import random
L=['самовар', 'весна', 'лето']
def Rn(L):
    s=random.choice(L)
    k=random.choice(s)
    st=s.replace(k,'?')
    print(st)
    j=input('Угадайте пропущенную букву : ')
    if j==k:
        print('Победа!\nСлово : ',s)
    else :
        print('Проигрыш(\nСлово : ',s)
Rn(L)

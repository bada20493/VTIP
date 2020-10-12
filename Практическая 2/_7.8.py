import random
def I():
    i1=random.randint(1,6)
    i2=random.randint(1,6)
    if i1==i2 :
        print('Ничья!\n У игрока №1 = '+str(i1)+'\n У игрока №2 = ',i2)
    elif i1>i2 :
        print('Победа игрока №1!\n У игрока №1 = '+str(i1)+'\n У игрока №2 = ',i2)
    elif i1<i2 :
        print('Победа игрока №1!\n У игрока №1 = '+str(i1)+'\n У игрока №2 = ',i2)
I()

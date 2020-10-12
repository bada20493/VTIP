import random
x=random.randint(0,10)
s=input('Введите число : ')
while s!='Выход':
    if x==int(s) :
        print('Победа!')
        s=input('Введите слово "Выход" ')
    elif x<int(s):
        s=input('Неправильно! Загаданное число меньше.\nВведите число : ')
    elif x>int(s):
        s=input('Неправильно! Загаданное число больше.\nВведите число : ')

import math
def y_m(x):
    """Вычисляем функцию по формуле x^4+4^x
    >>> y_m(1)
    7
    """
    return (x**4+4**x)
x=int(input('Введите x = '))
print('Функция = ', y_m(x))
if __name__=="__main__":
    import doctest
    doctest.testmod()

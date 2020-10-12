L = [-8, 8, 6.0, 5, 'строка', -3.1]
Sum=0
for i in range(len(L)):
    if (type(L[i])== int) or (type(L[i])== float):
        Sum=Sum+L[i]
print(Sum)

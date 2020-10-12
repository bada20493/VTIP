x=input('Введите число : ')
sum=0
for i in range(len(x)):
    if int(x[i])%2 !=0:
        sum=sum+int(x[i])**2
print(sum)

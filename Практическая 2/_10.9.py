s='Мой12 дядя 34 сам1ых честных2 1 правил'
summ=0
k=0
max=0
for i in range(len(s)):
    if (ord(s[i])>47) and (ord(s[i])<58):
        summ=summ+int(s[i])
        k=k+1
        if int(s[i])>max:
            max=int(s[i])
print(summ)
print(k)
print(max)

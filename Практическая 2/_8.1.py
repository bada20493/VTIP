s="У лукоморья 123 дуб зеленый 456"
#Другой вариант нахождения : print(s.find('я'))
#1
k=-1
for i in range(len(s)):
    if s[i]=='я':
        k=i
if k>-1 :
    print(k)
else : print('В данной строке нет буквы "я"')
#2
l=0
for i in range(len(s)):
    if (s[i]=='у') or (s[i]=='У'):
        l=l+1
print('Количество букв "у" в строке = ',l)
#3
if s.isalpha() == False : print(s.upper())
#4
if len(s)>4 : print(s.lower())
#5
s='О'+s[1:]
print(s)


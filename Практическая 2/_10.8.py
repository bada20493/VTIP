s='Собачки бежали быстрее всех'.split()
ma=0
for i in s:
    if ma<len(i):
        word=i
        ma=len(i)
print(word)

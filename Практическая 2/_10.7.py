s='Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'
s=s.split()
for i in range(len(s)-1):
    if (s[i].startswith('М')) or (s[i].startswith('м')):
        del s[i]
print(' '.join(s))

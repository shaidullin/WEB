s=str(input("Введите строку: "))
s1=' '.join(s)
snew=' '
s2=s1.split(' ')
for i in range (len(s2)):
    if s2[i]=='Л':
        snew+=s2[i]
print("Новая строка: ",snew)

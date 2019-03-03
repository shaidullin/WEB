s=str(input("Введите строку: "))
k=s.split(' ')
for i in range (len(k)):
    if (k[i][len(k[i])-1:])=='r':
        print(k[i])

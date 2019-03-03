import random
sum=0
kol=0
sp=random.sample(range(10),3)
for i in range(len(sp)):
    sum+=sp[i]
    kol+=1
    sr=sum/kol
print(sp)
print("Среднее арифметическое = ",sr)

    

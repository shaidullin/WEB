import random
sum=1
sp=random.sample(range(50),10)
for i in range(len(sp)):
    if sp[i]>1 and sp[i]<10:
        sum=sum*sp[i]
print(sp)
print("Результат умножения всех чисел меньше 10 = ",sum)
    

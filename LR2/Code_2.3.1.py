import random
s='3'
for i in range (5):
    k=random.randint(ord('0'),ord('9'))
    s+=chr(k)
print(s)

from math import*
a=float(input("Введите значение a: "))
b=float(input("Введите значение b: "))
c=float(input("Введите значение c: "))
d=float(input("Введите значение d: "))
k=float(input("Введите значение k: "))
if (c-a)!=0:
    y=abs(1-a*b**c-a*(b**2-c**2)+(b-c+a)*(12+b)/(c-a))
else:
    y=input(" деление на ноль ")
print("Результат = ",y)


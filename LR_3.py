groupmates = [
    {
        "name": u"Константин",
        "group": "БАП1801",
        "age": 18,
        "marks": [4, 4, 4, 5, 3]
    },
    {
        "name": u"Андрей",
        "group": "БАП1801",
        "age": 21,
        "marks": [3, 3, 4, 4, 5]
    },
    {
        "name": u"Мансур",
        "group": "БАП1801",
        "age": 19,
        "marks": [5, 2, 4, 4, 3]
    },
    {
        "name": u"Максим",
        "group": "БАП1801",
        "age": 18,
        "marks": [5, 5, 5, 4, 4]
    }
]
def pnt_students(students):
    zn=float(input('Введите минимальный допустимый ср.балл '))
    print(u"Имя студента".ljust(15),u"Группа".ljust(8),u"Возраст".ljust(8),u"Оценки".ljust(20))
    for j in students:
        a=j["marks"]
        sr=0
        su=0
        for i in a:
            su+=i
        sr=su/len(a)
        if sr>=zn:
            print(j["name"].ljust(15),j["group"].ljust(8),str(j["age"]).ljust(8),str(j["marks"]).ljust(20))
pnt_students(groupmates)

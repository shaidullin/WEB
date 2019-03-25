groupmates = [
    {
        "name": u"Maxim",
        "group":"bap1801",
        "age": 22,
        "marks":[4,4,5,5,4]
    },
    {
        "name": u"Misha",
        "group":"bap1801",
        "age": 19,
        "marks":[4,5,5,5,4]
    },
    {
        "name": u"Shiska",
        "group":"bap1801",
        "age": 18,
        "marks":[4,3,5,3,4]
    },
    {
        "name": u"Egor",
        "group":"bap1801",
        "age": 18,
        "marks":[4,4,5,5,3]
    }
]
def print_students(students):
    znach=float(input('Введите минимальный допустимый средний балл '))
    print(u"Имя студента".ljust(15),u"Группа".ljust(8),u"Оценки".ljust(20))
    pred=0
    for student in students:
        a=student["marks"]
        sr=su=0
        for i in a:
            su+=i
        sr=su/len(a)
        if sr>=znach:
            print(student["name"].ljust(15),student["group"].ljust(8),str(student["age"]).ljust(8),str(student["marks"]).ljust(20))
print_students(groupmates)

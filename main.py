import student
import classroom
import os
import random

classroom1 = classroom.Classroom()

for i in range(5):
    name = "próba"+str(i)
    age = 15 + i
    classroom1.add_new_student(name, age)
    for j in range(5):
        grade = random.randint(1,5)
        classroom1.students[i].add_grade(grade)

#os.system("cls")

run = True
while run:
    parancs = input("""
Mit szeretne csinálni?
e-exit
dh-diák hozzáadása
dt-diák törlése
jb-jegy beírása
ol-osztályátlag lekérdezése
dk-diákok kiíratása
""")

    if parancs == "e":
        print("A program leállt")
        run = False
        
    elif parancs == "dh":
        name1 = input("Mi legyen a diák neve?")
        age1 = input("Mi legyen a diák kora?")
        classroom1.add_new_student(name1, age1)
    
    elif parancs == "dt":
        name = input("Melyik diákot töröljük ki?")
        classroom1.delete_student(name)
        print("A diák törölve!")

    elif parancs == "jb":
        name = input("Melyik diáknak akar nevet beírni?")
        grade = int(input("Milyen jegyet szeretne beírni?"))
        classroom1.add_grade_to_student(name, grade)

    elif parancs == "ol":
        print(f"Az átlag: {classroom1.calc_avg_of_class()}")
        
    elif parancs == "dk":
        classroom1.write_out_students()

    else:
        print("Rossz parancsot adott meg, adjon meg egy másikat!")
        
        



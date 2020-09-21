import student
import classroom

classroom1 = classroom.Classroom()


run = True
while run:
    parancs = input("""
Mit szeretne csinálni?
e-exit
dh-diák hozzáadása
dk-diákok kiíratása
""")

    if parancs == "e":
        print("A program leállt")
        run = False
    elif parancs == "dh":
        name1 = input("Mi legyen a diák neve?")
        age1 = input("Mi legyen a diák kora?")
        classroom1.add_new_student(name1, age1)
        
    elif parancs == "dk":
        classroom1.write_out_students()
        
        



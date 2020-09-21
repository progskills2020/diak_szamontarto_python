import student

run = True

students = []

while run:
    input1 = input("""
    Mit szeretne csinálni?
    e-exit
    dh-diák hozzáadása
    dk-diákok kiíratása
    """)

    if input1 == "e":
        print("A program leállt")
        run = False
    elif input1 == "dh":
        name1 = input("Mi legyen a diák neve?")
        age1 = input("Mi legyen a diák kora?")
        student1 = student.Student(name1, age1)
        students.append(student1)
        print("A diák hozzáadva!")
    elif input1 == "dk":
        for student in range(len(students)):
            students[student].output_data()
        



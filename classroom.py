import student

class Classroom:
    def __init__(self):
        self.students = []

    def add_new_student(self, name, age):
        student1 = student.Student(name, age)
        self.students.append(student1)
        print("A diák hozzáadva!")

    def write_out_students(self):
        print("Az adatbázisban az alábbi diákok szerepelnek:")
        for student in range(len(self.students)):
            print(f"A(z) {student + 1}. diák neve {self.students[student].name} és kora {self.students[student].age} év.")


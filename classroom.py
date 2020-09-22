import student

class Classroom:
    def __init__(self):
        self.students = []

    def add_new_student(self, name, age):
        student1 = student.Student(name, age)
        self.students.append(student1)
        print("A diák hozzáadva!")

    def delete_student(self, name):
        for i in range(len(self.students)):
            if name == self.students[i].name:
                del self.students[i]
                break

    def add_grade_to_student(self, name, grade):
        for i in range(len(self.students)):
            if name == self.students[i].name:
                self.students[i].add_grade(grade)


    def write_out_students(self):
        print("Az adatbázisban az alábbi diákok szerepelnek:")
        for student in range(len(self.students)):
            print(f"A(z) {student + 1}. diák neve {self.students[student].name}, kora {self.students[student].age} év és átlaga {self.students[student].calc_avg_grade()}.")


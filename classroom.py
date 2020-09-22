import student

class Classroom:
    def __init__(self):
        self.students = []

    def calc_avg_of_class(self):
        if len(self.students) != 0:
            sum_of_grades_of_all_students = 0
            for i in range(len(self.students)):
                if self.students[i].calc_avg_grade() != "még nem számolható":
                    sum_of_grades_of_all_students += self.students[i].calc_avg_grade()
            avg = sum_of_grades_of_all_students/len(self.students)
            avg = round(avg, 2)
        else:
            avg = "nem számolható."
        return avg



    def add_new_student(self, name, age):
        student1 = student.Student(name, age)
        self.students.append(student1)
        print(f"{student1.name} nevű diák lett hozzáadva az adatbázishoz")

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


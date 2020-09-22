import human

class Student(human.Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grades = []
        self.avg_grade = 0
    
    def add_grade(self, grade):
        self.grades.append(grade)
        print("Jegy beírva!")

    def calc_avg_grade(self):
        sum_of_grades = 0
        if len(self.grades) != 0:
            for i in range(len(self.grades)):
                sum_of_grades += self.grades[i] 
                avg_of_grades = sum_of_grades/len(self.grades)
        else:
            avg_of_grades = "még nem számolható"
        return avg_of_grades
            


    

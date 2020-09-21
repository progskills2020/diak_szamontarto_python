import human

class Student(human.Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        grades = []
        avg_grade = 0
    def output_data(self):
        print(f"Ezt a diákot {self.name} hívják és {self.age} éves")

class SchoolClass:
    def __init__(self, amount_of_students):
        self.amount_of_students = amount_of_students
        self.dict_students = {}
        self.dict_averages = {}
        self.filling_the_dict(self.amount_of_students)

    def filling_the_dict(self, n):
        for student in range(n):
            name = input()
            grade = float(input())
            if name not in self.dict_students:
                self.dict_students[name] = [grade]
            else:
                self.dict_students[name].append(grade)
        self.average_for_student()

    def average_for_student(self):
        for name, grades in self.dict_students.items():
            average = sum(grades) / len(grades)
            if average >= 4.50:
                self.dict_averages[name] = average
        print(self.print_output())

    def print_output(self):
        result = ''
        for name, average_grade in sorted(self.dict_averages.items(), key= lambda x: -x[1]):
            result += f'{name} -> {average_grade:.2f}\n'
        return result


class_1 = SchoolClass(int(input()))

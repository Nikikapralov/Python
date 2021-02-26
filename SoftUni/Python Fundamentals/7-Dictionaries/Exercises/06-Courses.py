class Courses:
    def __init__(self):
        self.dict_courses = {}
        self.filling_the_dict()

    def filling_the_dict(self):
        while True:
            command = input()
            if command == 'end':
                print(self.print_output())
                break
            else:
                course_name_key, student_name_value = command.split(' : ')
            if course_name_key not in self.dict_courses:
                self.dict_courses[course_name_key] = [student_name_value]
            else:
                self.dict_courses[course_name_key].append(student_name_value)
        return

    def print_output(self):
        result = ''
        for course, students_list in sorted(self.dict_courses.items(), key=lambda x: -len(x[1])):
            result += f'{course}: {len(students_list)}\n'
            for student in sorted(students_list):
                result += f'-- {student}\n'
        return result


courses = Courses()
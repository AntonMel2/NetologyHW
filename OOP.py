def mid_grade_all_students(students_list, course):
    md_grade = 0
    count = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.grades:
            md_grade += student.grades.get(course)
            count += 1
    if count > 0:
        return md_grade / count
    else:
        return md_grade

def mid_grade_all_lectures(lecturers_list, course):
    md_grade = 0
    count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.lecturers_grades:
            md_grade += lecturer.lecturers_grades.get(course)
            count += 1
    if count > 0:
        return md_grade / count
    else:
        return md_grade


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _mid_grade_(self):
        md_grade = 0
        count = 0
        for key in self.grades.values():
            md_grade += key
            count += 1
        if count > 0:
            return md_grade / count
        else:
            return md_grade

    def __lt__(self, other):
        return self._mid_grade_() < other._mid_grade_()

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания: {self._mid_grade_()} \n"
                f"Курсы в процессе изучения: {','.join(self.courses_in_progress)} \n"
                f"Завершенные курсы: {','.join(self.finished_courses)}")


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturers_grades = {}

    def _mid_grade_(self):
        md_grade = 0
        count = 0
        for key in self.lecturers_grades.values():
            md_grade += key
            count += 1
        if count > 0:
            return md_grade / count
        else:
            return md_grade

    def __lt__(self, other):
        return self._mid_grade_() < other._mid_grade_()

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за лекции: {self._mid_grade_()}")


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname}")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']
best_student.grades.update({'Python': 10})
best_student.grades.update({'Java': 9})
print(best_student)
print()

worst_student = Student('Ivan', 'Ivanov', 'man')
worst_student.courses_in_progress += ['Python']
worst_student.grades.update({'Python': 1})
print(worst_student)
print()

print(best_student < worst_student)
print()

first_lecturer = Lecturer('Anton', 'Titov')
first_lecturer.lecturers_grades.update({'Python': 5})
print(first_lecturer)
print()

second_lecturer = Lecturer('Ivan', 'Belov')
second_lecturer.lecturers_grades.update({'Python': 9})
second_lecturer.lecturers_grades.update({'CSS': 10})
print(second_lecturer)
print()

print(first_lecturer < second_lecturer)

first_reviewer = Reviewer('Stepan', 'Petrosyn')
first_reviewer.courses_attached += ['HTML']
print(first_reviewer.rate_hw(best_student, 'HTML', 9))



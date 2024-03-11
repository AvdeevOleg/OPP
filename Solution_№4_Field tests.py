class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_hw(self, reviewer, course, grade):
        if isinstance(reviewer, Reviewer) and course in self.courses_in_progress and course in reviewer.courses_attached:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades) if self.grades else 0
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_grade:.1f}\n' \
               f'Курсы в процессе изучения: {in_progress_courses}\n' \
               f'Завершенные курсы: {finished_courses}'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other):
        return sum(sum(grades) / len(grades) for grades in self.grades.values()) < sum(
            sum(grades) / len(grades) for grades in other.grades.values())

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if not self.grades:
            return super().__str__() + f'\nСредняя оценка за лекции: Нет оценок'
        else:
            average_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
            return super().__str__() + f'\nСредняя оценка за лекции: {average_grade:.1f}'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other):
        return sum(sum(grades) / len(grades) for grades in self.grades.values()) < sum(
            sum(grades) / len(grades) for grades in other.grades.values())

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other


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
        return super().__str__()

def avg_grade_for_course_students(students, course):
    grades_sum = 0
    students_count = 0
    for student in students:
        if course in student.grades:
            grades_sum += sum(student.grades[course])
            students_count += len(student.grades[course])
    return grades_sum / students_count if students_count > 0 else 0

def avg_grade_for_course_lecturers(lecturers, course):
    grades_sum = 0
    lecturers_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades_sum += sum(lecturer.grades[course])
            lecturers_count += 1
    return grades_sum / lecturers_count if lecturers_count > 0 else 0

# Создаем объекты студента, рецензента и лектора
some_reviewer1 = Reviewer('Another', 'Buddy')
some_reviewer2 = Reviewer('John', 'Doe')

some_lecturer1 = Lecturer('Some', 'Buddy')
some_lecturer2 = Lecturer('Jane', 'Doe')

some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student2 = Student('Alice', 'Smith', 'female')

# Оценки для студента и лектора
some_reviewer1.rate_hw(some_student1, 'Python', 9)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 8)
some_reviewer2.rate_hw(some_student2, 'Python', 7)

# Добавим курсы студентам
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Введение в программирование']
some_student2.courses_in_progress += ['Python', 'Git']
some_student2.finished_courses += ['Введение в программирование']

# Вывод информации о рецензенте
print(some_reviewer1)
print(some_reviewer2)
print()

# Вывод информации о лекторе
print(some_lecturer1)
print(some_lecturer2)
print()

# Вывод информации о студенте
print(some_student1)
print(some_student2)
print()

# Вызов функций для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
course_name = 'Python'
print(f'Средняя оценка за домашние задания по курсу "{course_name}": {avg_grade_for_course_students([some_student1, some_student2], course_name):.1f}')

# Вызов функций для подсчета средней оценки за лекции всех лекторов в рамках курса
course_name = 'Python'
print(f'Средняя оценка за лекции по курсу "{course_name}": {avg_grade_for_course_lecturers([some_lecturer1, some_lecturer2], course_name):.1f}')

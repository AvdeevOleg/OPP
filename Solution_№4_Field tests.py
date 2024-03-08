class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_hw(self, reviewer, course, grade):
        if isinstance(reviewer,
                      Reviewer) and course in self.courses_in_progress and course in reviewer.courses_attached:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(
            self.grades) if self.grades else 0
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_grade:.1f}\n' \
               f'Курсы в процессе изучения: {in_progress_courses}\n' \
               f'Завершенные курсы: {finished_courses}'


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


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def avg_hw_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students != 0 else 0


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def avg_lecture_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += 1
    return total_grades / total_lecturers if total_lecturers != 0 else 0


# Создаем экземпляры классов
student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Emma', 'Johnson', 'female')

lecturer1 = Lecturer('John', 'Doe')
lecturer2 = Lecturer('Alice', 'Smith')

reviewer1 = Reviewer('Bob', 'Brown')
reviewer2 = Reviewer('Eva', 'Williams')

# Добавляем курсы
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

# Выставляем оценки
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 7)

student1.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 9)

# Выводим информацию
print("Студенты:")
print(student1)
print(student2)

print("\nЛекторы:")
print(lecturer1)
print(lecturer2)

print("\nПроверяющие:")
print(reviewer1)
print(reviewer2)

# Вызываем функции для подсчета средних оценок
print("\nСредняя оценка за домашние задания по курсу Python:", avg_hw_grade([student1, student2], 'Python'))
print("Средняя оценка за лекции по курсу Python:", avg_lecture_grade([lecturer1, lecturer2], 'Python'))

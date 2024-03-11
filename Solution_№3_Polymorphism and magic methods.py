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

    def rate_lecture(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

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
        average_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(
            self.grades) if self.grades else 0
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


# Создаем объекты студента, рецензента и лектора
some_reviewer = Reviewer('Another', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman', 'your_gender')

# Оценки для студента и лектора
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_lecturer.rate_lecture(some_student, 'Python', 9)
some_lecturer.rate_lecture(some_student, 'Python', 10)

# Добавим курсы студенту
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

# Вывод информации о рецензенте
print(some_reviewer)
print()

# Вывод информации о лекторе
print(some_lecturer)
print()

# Вывод информации о студенте
print(some_student)


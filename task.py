#класс Студенты
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    #метод выставление оценки лекторам
    def rate_for_lecturer(self, lecturer, course, grade):
        if grade <= 0 or grade > 10:
            print("Выставте оценку по  по 10-балльной шкале (от 1 до 10, где 1-минимальная, а 10 максимальная)")
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Не найдены данные о лекторе или о курсе'

    #метод подсчета средней оценки за домашную работу
    def get_avg_grade(self):
        sum_lect = 0
        count = 0
        for course in self.grades.values():
            sum_lect += sum(course)
            count += len(course)
        if count == 0:
            print(" нет оценок")
        else:    
            return round(sum_lect / count, 2) 

    #переопределение строки __str__, которую принимает на вход print
    def __str__(self):
        res = f'\nИмя: {self.name}\n'f'Фамилия: {self.surname} \n'f'Средняя оценка за домашние задания:{self.get_avg_grade()}\n'f'Курсы в процессе изучения: {self.courses_in_progress}\n'f'Завершенные курсы: {self.finished_courses}'
        return res 

    #переопределение метода lessthen, который теперь будет сравнивать объекты по признаку "средняя оценка"
    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Студент не найден')
            return
        else:
            if self.get_avg_grade() < other_student.get_avg_grade():
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            elif self.get_avg_grade() > other_student.get_avg_grade():
                print(f'{self.name} {self.surname} учится лучше, чем {other_student.name} {other_student.surname}')
            elif self.get_avg_grade() == other_student.get_avg_grade():
                print("Ученики учатся одинакого")

    #метод добавление ученика на курс
    def attach_course(self, courses):
        for course in courses:
            self.courses_in_progress.append(course)
    
    #метод завершения курса учеником
    def finished_course(self, courses):
        for course in courses:
            if course in self.courses_in_progress:
                self.courses_in_progress.remove(course)
                self.finished_courses.append(course)

#класс Менторы           
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

#класс Лекторы (назледник Ментора)       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 
        self.courses_attached = []   

    #переопределение строки __str__, которую принимает на вход print
    def __str__(self):
        res = f'\nИмя: {self.name}\n'f'Фамилия: {self.surname} \n'f'Средняя оценка за лекции: {self.get_avg_grade()}'
        return res 

    #метод подсчета средней оценки за проведение лекций
    def get_avg_grade(self):
        sum_lect = 0
        count = 0
        for course in self.grades.values():
            sum_lect += sum(course)
            count += len(course)
        if count == 0:
            print(" нет оценок")
        else:    
            return round(sum_lect / count, 2) 

    #переопределение метода > lessthen, который теперь будет сравнивать объекты по признаку "средняя оценка"        
    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет!')
            return
        else:
            compare = self.get_avg_grade() < other_lecturer.get_avg_grade()
            if self.get_avg_grade() < other_lecturer.get_avg_grade():
                print(f'{self.name} {self.surname} ведет хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            elif self.get_avg_grade() > other_lecturer.get_avg_grade():
                print(f'{self.name} {self.surname} ведет лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            elif self.get_avg_grade() == other_lecturer.get_avg_grade():
                print("Ведут одинакого")

    #метод добавление лектора на курс
    def attach_course(self, courses):
        for course in courses:
            self.courses_attached.append(course)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []   

    #метод выставление оценки ученикам
    def rate_hw(self, student, course, grade):
        if grade <= 0 or grade > 10:
            print("Выставте оценку по  по 10-балльной шкале (от 1 до 10, где 1-минимальная, а 10 максимальная)")
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    #метод добавление ревьюера на курс
    def attach_course(self, courses):
        for course in courses:
            self.courses_attached.append(course)

    def __str__(self):
        res = f'\nИмя: {self.name}\n'f'Фамилия: {self.surname}' 
        return res 


#создание экземпляров
student1 = Student("Наталья","Мухина","ж")
student2 = Student("Виталий","Жуков","м")

lector1 = Lecturer("Лектор","Лекторович")
lector2 = Lecturer("СекондЛектор","Секондоривич")

reviewer1 = Reviewer ("Провер","Проверин")
reviewer2 = Reviewer ("Ревьер","Ревьюерин")

#назначаем всем курсы
student1.attach_course(["Курс1","Курс2","Курс3"])
student1.finished_course(["Курс3"])
student2.attach_course(["Курс1","Курс2","Курс3"])

lector1.attach_course(["Курс1","Курс2","Курс3"])
lector2.attach_course(["Курс1","Курс2","Курс3"])

reviewer1.attach_course(["Курс1","Курс2","Курс3"])
reviewer2.attach_course(["Курс1","Курс2","Курс3"])

#ученики оценивают лекторов
student1.rate_for_lecturer(lector1, 'Курс1', 6)
student1.rate_for_lecturer(lector1, 'Курс2', 9)
student1.rate_for_lecturer(lector1, 'Курс2', 7)
student2.rate_for_lecturer(lector1, 'Курс1', 9)
student2.rate_for_lecturer(lector1, 'Курс2', 9)
student2.rate_for_lecturer(lector2, 'Курс3', 0)
student2.rate_for_lecturer(lector2, 'Курс2', 9)
student2.rate_for_lecturer(lector2, 'Курс1', 5)

#проверяющие оценивают работы учеников
reviewer1.rate_hw(student1, 'Курс1', 8)
reviewer1.rate_hw(student2, 'Курс1', 9)
reviewer1.rate_hw(student1, 'Курс1', 5)
reviewer1.rate_hw(student1, 'Курс2', 8)
reviewer2.rate_hw(student1, 'Курс2', 13)
reviewer2.rate_hw(student1, 'Курс3', 7)

#Выводим информацию об объектах
print(student1)
print(lector1)
print(reviewer1)
print('\n')

#сравниваем студентов
print(student1 > student2)

#сравниваем лекторов
print(lector1 < lector2)

# средняя оценка за доманшние задание по курсу
def get_avg_hw_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)

student_list = [student1, student2]
hm_course = "Курс1"
print(f'Средняя оценка за ДЗ по курсу "{hm_course}": {get_avg_hw_grade(student_list, hm_course)}')

# средняя оценка за лекции лекторов по курсу
def get_avg_lector_grade(lector_list, course):
    total_sum = 0
    for student in lector_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(lector_list), 2)

lector_list = [lector1, lector2]
lc_course = "Курс2"
print(f'Средняя оценка лекторов по курсу "{lc_course }": {get_avg_lector_grade(lector_list, lc_course)}')

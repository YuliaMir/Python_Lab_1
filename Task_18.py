'''Разработать систему решения задач учениками курса «Разработчик на Питоне» и
проверке их преподавателем.'''


class Task:
    def __init__(self, description):
        self.description = description
        self.status = "unsolved"

class Teacher:
    def __init__(self, name):
        self.name = name

    def check_task(self, student, task):
        if task.status == "solved":
            task.status = "resolved"
            return f"Задание '{task.description}' от {student.name} было выполнено."
        else:
            task.status = "unsolved"
            return f"Задание '{task.description}' от {student.name} было не выполнено."

class Student:
    def __init__(self, name):
        self.name = name

    def solve_task(self, task):
        task.status = "solved"
        return f"Задание '{task.description}' было выполнено студентом {self.name}."

task1 = Task("Рекурсия")
teacher = Teacher("Иван Иванович")
student1 = Student("Ася")

print(f"Преподаватель назначает задание: '{task1.description}' студенту {student1.name}")
print(student1.solve_task(task1))

print(teacher.check_task(student1, task1))

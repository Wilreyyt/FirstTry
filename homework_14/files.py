"""Файлы"""


import os.path


class Student:
    """Студент"""
    def __init__(self, name: str, group: str, grades: list[int]):
        self.name = name
        self.group = group
        self.grades = grades

    def to_str(self) -> str:
        """Преобразовать студента в строку"""
        return f"{self.name} | {self.group} | {self.grades}\n"


def read_student_from_string(string: str) -> Student:
    """Создать студента из строки"""
    words = string.split("|")

    str_grades = words[2].strip()
    str_grades = str_grades[1:-1]

    grades = str_grades.split(',')
    result_grades = []
    for grade in grades:
        result_grades.append(int(grade.strip()))

    return Student(
        words[0].strip(),
        words[1].strip(),
        result_grades
    )


def get_count_by_groups(studens: list[Student]) -> dict[str, int]:
    """Посчитать количество студентов по группам"""
    result = dict()
    for student in studens:
        if student.group not in result:
            result[student.group] = 0

        result[student.group] += 1

    return result


def read_students_from_file(file_path: str) -> list[Student]:
    """Прочитать студентов из файла"""
    students_from_file = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            if line == '\n':
                continue
            if line.startswith("Number of students"):
                return students_from_file

            student = read_student_from_string(line)
            students_from_file.append(student)

    return students_from_file


def main():
    """Основной код программы"""
    file_path = "students.txt"

    students = [
        Student("Maxim Lazar", "Group 1", [7, 8, 6, 7, 9]),
        Student("Kurnos Kuzovatov", "Group 1", [4, 7, 3, 5, 8, 7, 6]),
        Student("Ernest Hemingway", "Group 1", [7, 7, 7, 5, 9]),
        Student("Stepan Bogdan", "Group 2", [10, 8, 5, 6, 7, 8, 10]),
        Student("Vladimir Trekatol", "Group 2", [6, 7, 9, 9]),
    ]

    if not os.path.exists(file_path):
        print("Запись в файл")
        with open(file_path, "w") as file:
            for student in students:
                file.write(student.to_str())

    print("Чтение из файла")
    try:
        students_from_file = read_students_from_file(file_path)
    except Exception:
        print("Произошла ошибка при чтении студентов из файла. "
              "Некорректный формат")
        return

    print("Число студентов в файле:", len(students_from_file))

    students_by_groups = get_count_by_groups(students_from_file)
    print("Количество студентов по группам:", students_by_groups)

    has_statistics = False
    with open(file_path, "r") as file:
        for line in file.readlines():
            if "Number of students:" in line:
                has_statistics = True

    if not has_statistics:
        with open(file_path, "a") as file:
            file.write(f"\nNumber of students: {len(students_from_file)}\n\n")

            file.write("Student count by groups\n")
            for group, count in students_by_groups.items():
                file.write(f"{group}: {count}\n")


main()

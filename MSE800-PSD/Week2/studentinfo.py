# Student Information Management System
# This program collects student data (name, age, student ID) for multiple students
# and displays them sorted by student ID.

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

def collect_students(num_students):
    students = []
    for i in range(num_students):
        name = input(f"Enter name for student {i+1}: ")
        age = int(input(f"Enter age for student {i+1}: "))
        student_id = input(f"Enter student ID for student {i+1}: ")
        students.append(Student(name, age, student_id))
    return students

def print_students(students):
    sorted_students = sorted(students, key=lambda s: int(s.student_id))
    print("List of students (sorted by student ID):")
    for student in sorted_students:
        print(f"Student ID: {student.student_id}, Name: {student.name}, Age: {student.age}")

if __name__ == "__main__":
    num_students = 3  # Collecting data for at least three students
    students = collect_students(num_students)
    print_students(students)
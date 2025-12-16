"""
Student Database Management System (CLI)
---------------------------------------
Features:
- Add, update, delete, search student records
- File-based storage using JSON
- Input validation
- OOPS-based clean structure
"""

import json
import os

DATA_FILE = "students.json"


class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }


class StudentDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student ID already exists!")
            return
        self.students[student.student_id] = student.to_dict()
        self.save_data()
        print("Student added successfully.")

    def update_student(self, student_id, name=None, age=None, course=None):
        if student_id not in self.students:
            print("Student not found!")
            return
        if name:
            self.students[student_id]["name"] = name
        if age:
            self.students[student_id]["age"] = age
        if course:
            self.students[student_id]["course"] = course
        self.save_data()
        print("Student updated successfully.")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found!")
            return
        del self.students[student_id]
        self.save_data()
        print("Student deleted successfully.")

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if not student:
            print("Student not found!")
            return
        print("\nStudent Details")
        print("---------------")
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")

    def display_all_students(self):
        if not self.students:
            print("No records found.")
            return
        print("\nAll Students")
        print("------------")
        for student in self.students.values():
            print(student)


class StudentApp:
    def __init__(self):
        self.db = StudentDatabase(DATA_FILE)

    def get_student_input(self):
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        course = input("Enter Course: ").strip()

        if not student_id or not name or not age.isdigit() or not course:
            print("Invalid input! Please try again.")
            return None

        return Student(student_id, name, int(age), course)

    def menu(self):
        while True:
            print("\nStudent Database Management System")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Search Student")
            print("5. Display All Students")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                student = self.get_student_input()
                if student:
                    self.db.add_student(student)

            elif choice == "2":
                student_id = input("Enter Student ID to update: ")
                name = input("New Name (leave blank to skip): ")
                age = input("New Age (leave blank to skip): ")
                course = input("New Course (leave blank to skip): ")

                self.db.update_student(
                    student_id,
                    name if name else None,
                    int(age) if age.isdigit() else None,
                    course if course else None
                )

            elif choice == "3":
                student_id = input("Enter Student ID to delete: ")
                self.db.delete_student(student_id)

            elif choice == "4":
                student_id = input("Enter Student ID to search: ")
                self.db.search_student(student_id)

            elif choice == "5":
                self.db.display_all_students()

            elif choice == "6":
                print("Exiting application...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = StudentApp()
    app.menu()

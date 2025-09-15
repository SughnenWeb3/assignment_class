class Student:
    def __init__(self, name: str, email: str, phone_number: int):
        self.name: str = name
        self.email: str = email
        self.phone_number: int = phone_number
        self.courses: list[str] = []

    def enroll(self, course: str) -> None:
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def show_courses(self):
        if self.courses:
            print(f"{self.name}'s courses:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print(f"{self.name} has not enrolled in any course yet.")


class ELearningSystem:
    def __init__(self, platform_name: str):
        self.platform_name: str = platform_name
        self.students: dict[str, Student] = {}

    def register_student(self, name: str, email: str, phone_number: int):
        if name not in self.students:
            student = Student(name, email, phone_number)
            self.students[name] = student
            print(f"Student '{name}' registered on {self.platform_name}")
        else:
            print(f"{name} is already registered.")

    def enroll_student_in_course(self, name: str, course: str):
        if name in self.students:
            self.students[name].enroll(course)
        else:
            print(f"{name} is not registered on {self.platform_name}")

    def show_all_students(self) -> None:
        print(f"\n--- Students on {self.platform_name} ---")
        for student in self.students.values():
            print(f"Name: {student.name}, Email: {student.email}, Phone: {student.phone_number}")
            student.show_courses()


system = ELearningSystem("BlockFuse Academy")

system.register_student("Alice", "alice@example.com", 123456789)
system.register_student("Bob", "bob@example.com", 987654321)

system.enroll_student_in_course("Alice", "Python Basics")
system.enroll_student_in_course("Alice", "AI for Beginners")
system.enroll_student_in_course("Bob", "Web Development")

system.show_all_students()

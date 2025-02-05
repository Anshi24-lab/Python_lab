class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Total: {sum(self.marks)}, Average: {self.average():.2f}")

# Creating three student objects
s1 = Student("Amit", 1, [85, 90, 80])
s2 = Student("Rahul", 2, [75, 80, 70])
s3 = Student("Priya", 3, [95, 85, 88])

# Displaying details
s1.display()
s2.display()
s3.display()


print("==============================")


class Student:
    def __init__(self):
        self.name = ""
        self.rollno = 0
        self.marks = []

    def accept_details(self):
        self.name = input("Enter student name: ")
        self.rollno = int(input("Enter roll number: "))
        self.marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]

    def calculate_average(self):
        total = sum(self.marks)
        avg = total / 3
        print(f"\nStudent: {self.name} | Roll No: {self.rollno}")
        print(f"Total Marks: {total} | Average Marks: {avg:.2f}")

# Creating and displaying details of three students
students = [Student() for _ in range(3)]
for student in students:
    student.accept_details()

print("\nFinal Results:")
for student in students:
    student.calculate_average()

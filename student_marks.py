class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)

students = [
    Student("John", [85, 78, 92]),
    Student("Alice", [88, 79, 95]),
    Student("Bob", [70, 75, 80])
]

average_marks = {student.name: student.average() for student in students}
top_performer = max(average_marks, key=average_marks.get)


print("Average Marks:", average_marks)
print("Top Performer:", top_performer)

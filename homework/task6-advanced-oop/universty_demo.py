from student import Student
# importing student class
from instructor import Instructor
# importing instructor class
from course import Course
# importing course class
from enrollment import Enrollment
# importing enrollment class
from teaching_assistant import TeachingAssistant
# importing teaching_assistant class

student1 = Student("bayishimiresamuel", "bayishimi samu@gmail.com")
instructor1 = Instructor("Dr. Pelin", "samuel pelin@gmail.com")
teach_assistant1 = TeachingAssistant("ernest", "ernest@gmail.com")

course1 = Course("Python")

Enrollment(student1, course1)
Enrollment(teach_assistant1, course1)

print(student1)
print(instructor1)

print(teach_assistant1)
print(course1)

print("Students in course:")
for student in course1.students:
    print("-", student.name)

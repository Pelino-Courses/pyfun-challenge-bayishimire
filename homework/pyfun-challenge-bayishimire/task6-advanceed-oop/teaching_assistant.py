from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
   # teaching assistance
    
    def __init__(self, name: str, email: str):
        Student.__init__(self, name, email)
        Instructor.__init__(self, name, email)

    def __str__(self):
        return f"Teaching Assistant details is : {self.name} ({self.email})"


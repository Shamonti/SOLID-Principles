class Student:
  def __init__(self, name, id, grades):
    self.name = name
    self.id = id
    self.grades = grades

class EmailService:
  def send_email(self, student):
    print(f"Sending welcome email to {student.name}")

class GPACalculator:
  def gpa_calculator(self, student):
    print(f"GPA for {student.name}: {sum(student.grades) / len(student.grades)}")

student = Student("Bob", 123, [90, 85, 88])
email_service = EmailService()
email_service.send_email(student)
gpa_calculator = GPACalculator()
gpa_calculator.gpa_calculator(student)
student2 = Student("Alice", 123, [95, 92])
email_service = EmailService()
email_service.send_email(student2)
gpa_calculator = GPACalculator()
gpa_calculator.gpa_calculator(student2)
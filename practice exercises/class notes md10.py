# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#             self.balance +=amount
#             print(f"Your new balance is {self.balance}")
#
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance += amount
#             print(f"Your current balance is {self.balance}")
#         else:
#             print("Not enough balance")
#
#     def show_balance(self):
#         print(f"Owner: {self.owner}")
#         print(f"Balance: {self.balance}")
#
#
# #main program
# account =  BankAccount("Maria", 1000)
# account.deposit(200)
# account.withdraw(500)
# account.withdraw(1000)
# account.show_balance()


# class exercise Association
# class Dog:
#     def __init__(self,name,birth_year,sound="Woof Woof"):
#         self.name = name
#         self.birth_year = birth_year
#         self.sound = sound
#
#     def bark(self,times):
#         for i in range(times):
#             print(self.name + "barks: " + self.sound)
#             return
# class Hotel:
#     def __init__(self):
#         self.dogs = []



# class Student:
#     def __init__(self, name, last_name, present = False):
#         self.name = name
#         self.last_name = last_name
#         self.present = present
#
# class Teacher:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def take_attendance(self):
#         for student in self.students:
#             if student.present:
#                 print(f"{student.name} {student.last_name}: Present")
#             else:
#                 print(f"{student.name} {student.last_name}: Absent")
#
#
# student1= Student("Kathy", "Musikka", True)
# student2= Student("Alip", "Tursun", False)
# teacher = Teacher()
# teacher.add_student(student1)
# teacher.add_student(student2)
#
# teacher.take_attendance()








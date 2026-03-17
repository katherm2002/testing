# class Dog:
#     pass
#
# dog = Dog()
# dog.name = "Terry"
# dog.birth_year = 2020
# print(f"{dog.name} is my cute dog and it was born in {dog.birth_year}")
#
# print("Hello!")
# class Dog:
#     def __init__(self,name,age,sound="woof woof"):
#         self.name = name
#         self.age = age
#         self.sound = sound
#     def bark(self,times):
#         for i in range(times):
#             print(self.sound)
#         return
# dog1 = Dog( "Tyson",4)
# dog2 = Dog("Bruno",5)
# dog1.bark(3)
# dog2.bark(2)
#
# print(f"{dog1.name} is my cute dog and it is {dog1.age} years old")
# print(f"{dog2.name} is my cute dog and it is {dog2.age} years old")

class Student:
    def __init__(self, name, student_id, city):
        self.name = name
        self.student_id = student_id
        self.city = city
    def intro(self):
        print(f"Hello, my name is {self.name} and i am from {self.city}")
students= []
number = int(input("Enter the number of student objects you want to create: "))
for i in range(number):
    print


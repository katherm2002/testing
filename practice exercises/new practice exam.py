# Exercise 1
# numbers=[]
# for i in range(3):
#     num=int(input("Enter a number: "))
#     numbers.append(num)
# print(f"The sum is: {sum(numbers)}")
# print(f"The largest number is: {max(numbers)}")
# print(f"The smallest number is: {min(numbers)}")

# Exercise 2
# age=int(input("Enter your age: "))
# citizenship=int(input("Are you a Finnish citizenship? \n1.Yes \n2.No"
#                       "\nChoose a number: "))
# if age < 18:
#     years_left= 18 - age
#     print(f"You have to wait {years_left} to vote.")
# elif citizenship != 1:
#     print("Not eligible due to citizenship")
# else:
#     print("You can vote!")

# Exercise 3
# numbers=[]
# user=input("Enter a number (empty to quit): ")
# while user != '':
#     numbers.append(int(user))
#     user = input("Enter a number (empty to quit): ")
#
# positive=0
# negative=0
# zeros=0
#
#
# for i in numbers:
#     if i > 0:
#         positive+=1
#     elif i < 0:
#         negative+=1
#     else:
#         zeros+=1
# print(f"You entered {len(numbers)} numbers.")
# print(f"positive numbers: {positive}.")
# print(f"negative numbers: {negative}.")
# print(f"zeros: {zeros}.")


# Exercise 4
# n=int(input("Enter a positive integer: "))
# if n <= 0:
#     print("Error")
# else:
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


# Exercise 5
# numbers=[]
# user=input("Enter a number (empty to quit): ")
# while user != '':
#     numbers.append(int(user))
#     user = input("Enter a number (empty to quit): ")
# numbers.sort()
# print(f"The second largest number is: {numbers[-2]}")
# print(f"The second smallest number is: {numbers[1]}")

# Exercise 6
# numbers=[]
# unique_numbers=set()
# user=int(input("Enter a number (Enter 0 to quit): "))
# while user != 0:
#     numbers.append(user)
#     user = int(input("Enter a number (Enter 0 to quit): "))
# for i in numbers:
#     if i not in unique_numbers:
#         unique_numbers.add(i)
# for a in unique_numbers:
#     if a > 10:
#         print(a)

# Exercise 7
# grades={}
# while True:
#     user = int(input("\nMenu: \n1.Add a student \n2.Fetch a student's grade"
#                      "\n3. Quit \nChoose a number: "))
#     if user == 1:
#         name=input("Enter student name: ")
#         score=int(input("Enter student score: "))
#         grades[name]=score
#         print("Data added")
#     elif  user == 2:
#         name=input("Enter student name: ")
#         if name in grades:
#             print(f"{name}: {grades[name]}")
#         else:
#             print("Student does not exist")
#     else:
#         print("Thank you for using our database")
#         break




# Exercise 8
# week_days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# user=int(input("Enter a week number from 1 to 7: "))
# if 1 <= user <= 7:
#     print(f"{week_days[user-1]}")
# else:
#     print("Invalid option")


# Exercise 9:
# def average(lst):
#     return sum(lst) / len(lst)
# numbers=[1,2,3,4,5,6]
# result=average(numbers)
# print(result)

# Exercise 10:
# names=set()
# user=input("Enter name (empty to quit): ")
# while user != '':
#     if user not in names:
#         print("New name")
#         names.add(user)
#     else:
#         print("Existing name")
#     user = input("Enter name (empty to quit): ")
# for i in names:
#     sorted(i)
#     print(i)


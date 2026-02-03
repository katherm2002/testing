# # Exercise 1
# print("Welcome!")
# first_name=input("Enter your first name: ")
# last_name=input("Enter your last_name: ")
# age=int(input("Enter your age: "))
# print(f"Hello {first_name.title()} {last_name.title()}, You are {age} years old.")
#

# Exercise 2
# import math
# radius_circle=float(input("Enter the radius of a circle: "))
# side_length_square=float(input("Enter the side length of a square: "))
# area_circle=math.pi * radius_circle ** 2
# area_square=side_length_square ** 2
# print(f"The area of the circle is {area_circle:.2f}")
# print(f"The area of the square is {area_square:.2f}")
# print("Thank you for using our program! \nGoodbye!")


# exercise 3
# n=int(input("Enter a number: "))
# if n > 0:
#     print(f"{n} is a positive number.")
# elif n < 0:
#     print(f"{n} is a negative number")
# else:
#     print(f"{n} is zero")


# exercise 4
# numbers=[]
# count=0
# user=input("Enter a number 'empty to quit': ")
# while user != '':
#     numbers.append(int(user))
#     count+=1
#     user = input("Enter a number 'empty to quit': ")
# total=sum(numbers)
# print(f"The sum of the numbers is {total}")
# print(f"You entered {count} numbers")



# exercise 5
# sum=0
# count=0
# while sum < 500:
#     user = int(input("Enter a number: "))
#     sum+=user
#     count+=1
# print(f"The final sum is {sum}")
# print(f"You entered {count} numbers")


# exercise 6
# user=int(input("Enter a positive number: "))
# if user <= 0:
#     print("Error")
# else:
#     for i in range(0,user+1,2):
#         print(i)
#

# exercise 7
# scores=[]
# user=int(input("Enter how many students there are: "))
# for i in range(user):
#     exam_scores=int(input("Enter exam scores (0-100): "))
#     scores.append(exam_scores)
# average=sum(scores) / user
# count=0
# for a in scores:
#     if a >= 90:
#         count+=1
# print(f"The average score is {average}")
# print(f"The highest score is {max(scores)}")
# print(f"The lowest score is {min(scores)}")
# print(f"There are {count} scores greater than or equal to 90")


# exercise 8
# numbers=[]
# unique_numbers=set()
# user=int(input("Enter number: "))
# while user != 0:
#     numbers.append(user)
#     user = int(input("Enter number: "))
# for i in numbers:
#     unique_numbers.add(i)
# print(unique_numbers)


# exercise 9
# phonebook={}
# print(f"Welcome to the phonebook!")
# while True:
#     user=int(input("Check options \n1. Add a new contact"
#            "\n2. Search for a contact \n3. Quit"
#            "\nChoose a number: "))
#     if user == 1:
#         name=input("Enter name: ")
#         phone_number=int(input("Enter phone number: "))
#         phonebook[name]=phone_number
#     elif user == 2:
#         name=input("Enter name: ")
#         if name in phonebook:
#             print(f"The phone number is {phonebook[name]}")
#         else:
#             print(f"Not in the sistem")
#     elif user == 3:
#         print(f"Thank you for using our service!")
#         break
#     else:
#         print("Invalid option")

# exercise 10
# seasons=("spring","summer","autumn","winter")
# print("Welcome to finnish season!")
# user=int(input("Check the months: \n 1.January"
#                "\n 2.February \n 3.March"
#                "\n 4.April \n 5.May \n 6.June \n 7.July \n 8.August"
#                "\n 9.September \n 10.October \n 11.November \n 12.December"
#                "\nChoose a month number: "))
# if user == 12 or user == 1 or user == 2:
#     print(f"The season for the month number {user} is winter.")
#     print("You need to buy a winter jacket!")
# elif user == 3 or user == 4 or user == 5:
#     print(f"The season for the month number {user} is spring.")
#     print("Finally sun is out!")
# elif user == 6 or user == 7 or user == 8:
#     print(f"The season for the month number {user} is summer.")
#     print("It's time to go to the beach!")
# elif user == 9 or user == 10 or user == 11:
#     print(f"The season for the month number {user} is autumn.")
#     print("Time to wear leather jacket!")
# else:
#     print("Invalid option")


# exercise 11
# def num(lst):
#     return sum(lst)
# numbers=[2,3,4,5,6,7,8]
# result=num(numbers)
# print(result)

# bonus
# names=set()
# user = input("Enter a name 'empty to quit': ")
# while user != '':
#     if user in names:
#         print("Existing name")
#     else:
#         print("New name")
#         names.add(user)
#     user = input("Enter a name 'empty to quit': ")
# for x in names:
#     print(x)




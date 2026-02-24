# Exercise 1
# amount=int(input("How many products you bought?: "))
# price=float(input("What's the price of the product: €"))
# total_price=amount * price
# print(f"Total price without VAT: €{total_price}")
# print(f"Total price with VAT: €{total_price + (total_price * 0.24)}")
#


# Exercise 2
# meters=float(input("Enter meters: "))
# cm= meters * 100
# millimeters= cm * 1000
# print(f"The distance in cm is: {cm}")
# print(f"The distance in millimeters: {millimeters}")


# Exercise 3
# weather= float(input("Enter the outside temperature: "))
# if weather < 0:
#     print(f"Freezing")
# elif 0 <= weather <= 10:
#     print(f"Cold")
# elif 11 <= weather <= 20:
#     print("Mild")
# else:
#     print("Warm")

# Exercise 4 no idea
# numbers=[]
# user=input("Enter a number (empty to quit): ")
# while user != '':
#     numbers.append(int(user))
#     user = input("Enter a number (empty to quit): ")
# print(f"The smallest number {min(numbers)} \n"
#       f"The largest number {max(numbers)}")



# Exercise 5
# total=0
# count=0
#
# while total < 100:
#     prices = float(input("Enter prices: "))
#     total+=prices
#     count+=1
#
# print(f"The total sum: {total}")
# print(f"You entered {count} prices")

# Exercise 6
# import random
# a=random.randint(0,9)
# b=random.randint(0,9)
# c=random.randint(0,9)
# d=random.randint(0,9)
#
# code=str(a)+str(b)+str(c)+str(d)
# print(f"Your security code is: {code}")


# Exercise 7 no se
# import random
# total=0
# user=int(input("How many time do you want to roll a die: "))
# for i in range(user):
#     roll= random.randint(1,6)
#     total += roll
# print(f"The total sum is {total}")


#Exercise 8
# numbers=[]
# user=input("Enter numbers (empty to quit): ")
# while user != '':
#     numbers.append(int(user))
#     user = input("Enter numbers (empty to quit): ")
# numbers.sort()
# print(f"The three greatest numbers are: {numbers[-1]} {numbers[-2]} {numbers[-3]}")

# Exercise 9
# def euros_to_cents(euros):
#     return euros * 100
# user=int(input("Enter euro value: "))
# result=euros_to_cents(user)
# print(f"{result} cents")

# Exercise 10
# def divisible(lst):
#     count=0
#     for i in lst:
#         if i % 3 == 0:
#             count+=1
#     return count
# numbers=[1,2,3,4,5,10,12,15]
# result=divisible(numbers)
# print(result)


# Exercise 11
# seasons= ("spring","summer","autumn","winter")
# user=int(input("Enter a month number (1-12): "))
# if user == 12 or user == 1 or user == 2:
#     print(f"The season is {seasons[3]}")
# elif user == 3 or user == 4 or user == 5:
#     print(f"The season is {seasons[0]}")
# elif user == 6 or user == 7 or user == 8:
#     print(f"The season is {seasons[1]}")
# elif user == 9 or user == 10 or user == 11:
#     print(f"The season is {seasons[2]}")
# else:
#     print("Invalid option")


# Exercise 12
# names=set()
# user=input("Enter a name (empty to quit): ")
# while user != '':
#     if user not in names:
#         names.add(user)
#         print("New name")
#     else:
#         print("Existing name")
#     user = input("Enter a name (empty to quit): ")
#
# for i in names:
#     print(i)

# Exercise 13
# grades={}
# while True:
#     user=int(input(f"\nMenu: \n1.Add/update a grade"
#                    f"\n2.Fetch a grade \n3.Print all students (name + grade)"
#                    f"\n4. Quit \nChoose a number: "))
#     if user == 1:
#         student_name=input("Enter student name: ")
#         grade=int(input("Enter student grade: "))
#         grades[student_name]=grade
#         print(f"Data added")
#     elif user == 2:
#         student_name=input("Enter student name: ")
#         if student_name in grades:
#             print(f"{student_name}: {grades[student_name]}")
#         else:
#             print(f"Student name not in the system")
#     elif user == 3:
#         for name in grades:
#             print(name, grades[name])
#     elif user == 4:
#         print(f"Thank you for using our database")
#         break
#     else:
#         print("Invalid option")

def sum_of_list(lst)
    return sum(lst)
number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")
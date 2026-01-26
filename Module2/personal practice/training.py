# EXERCISE 1
# name =input("Enter your first name and last time: ")
# print(f"Hello, {name}!")

# EXERCISE 2
# length= float(input("Enter the length of a rectangle: "))
# width= float(input("Enter the width of a rectangle: "))
# perimeter= 2 * (length + width)
# area= length * width
# print(f"The perimeter of the rectangle is {perimeter}")
# print(f"The area of the rectangle is {area}")

# EXERCISE 3
# a=int(input("Enter first integer number: "))
# b=int(input("Enter second integer number: "))
# c=int(input("Enter third integer number: "))

# sum_numbers=a+b+c
# product=a*b*c
# average=sum_numbers/3

# print(f"The sum is: {sum_numbers}")
# print(f"The product is: {product}")
# print(f"The average is: {average}")

# EXERCISE 4
# import math
# radius_circle=float(input("Enter radius of circle: "))
# length_square=float(input("Enter length of square: "))
# area_circle=math.pi * radius_circle ** 2
# area_square= length_square * length_square
# print(f"The are of the circle is: {area_circle}")
# print(f"The are of the square is: {area_square}")

# EXERCISE 5
# banana=float(input("Enter the amount of bananas in kg: "))
# apple=float(input("Enter the amount of apples in kg: "))
# orange=float(input("Enter the amount of oranges in kg: "))
#
# price_banana=banana*2.85
# price_apple=apple*3.15
# price_orange=orange*4.05
# total_price=price_banana+price_apple+price_orange
#
# print(f"The price of bananas is: {price_banana:.2f}")
# print(f"The price of apples is: {price_apple:.2f}")
# print(f"The price of oranges is: {price_orange:.2f}")
# print(f"The total of prices is: {total_price:.2f}")

# EXERCISE 6
# import random
#
# die1 = random.randint(1, 6)
# die2 = random.randint(1, 20)
#
# print("Six-sided die:", die1)
# print("Twenty-sided die:", die2)
# print("Total:", die1 + die2)


# EXERCISE 7
# user_age=int(input("Enter your age: "))
# if user_age>=18:
#     print("You are old enough to vote")
# else:
#     years_left=18-user_age
#     print(f"You can vote in {years_left} years.")

# EXERCISE 8
# consumption=float(input("Please enter your electricity consumption in kWh: "))
# if consumption<=50:
#     bill=consumption*0.10
# elif consumption<=200:
#     bill=50*0.10+(consumption-50)*0.08
# else:
#     bill=50*0.10+150*0.08+(consumption-200)*0.06
#
# print(f"Electricity bill: € {bill:.2f}")

# EXERCISE 9
# score_physics=int(input("Enter your physics score: "))
# score_mathematics=int(input("Enter your mathematics score: "))
# score_chemistry=int(input("Enter your chemistry score: "))
# if score_physics < 50 or score_mathematics < 50 or score_chemistry < 50:
#     print("You don't get scholarship.")
# elif (score_physics > 90 and score_mathematics > 90) or score_chemistry > 95:
#     print("You get scholarship.")
# else:
#     print("You don't get scholarship.")


# EXERCISE 10
# user_year=int(input("Enter a year: "))
# if user_year % 4 == 0 and user_year % 100 !=0 or user_year % 400 == 0:
#     print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")


# WHILE EXERCISES
# user_number=int(input("Please enter a number: "))
# while user_number>=0:
#     print(f"You entered: {user_number}")
#     user_name=int(input("Please enter a number: "))
# print(f"program ended.")

# WHILE EXERCISES
# total=0
# count=0
# while total <= 100:
#     number=int(input("Enter a number: "))
#     total+=number
#     count+=1
# print(f"Final sum: {total}")
# print(f"you entered: {count} numbers")


# WHILE EXERCISES
# inches=float(input("Enter inches: "))
# while inches >= 0:
#     centimeters=inches*2.54
#     print(f"centimeters: {centimeters} ")
#     inches=float(input("Enter inches: "))
# print(f"program ended")


# BREAK EXERCISES
# while True:
#     number = int(input("Please enter a number: "))
#     if number == 0:
#         break
#     print(f"The number you entered is {number}")












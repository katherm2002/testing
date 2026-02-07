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


# EXERCISES PRACTICE
# name= input("Enter name: ")
# print(f"Hello, {name.title()}!")


# next
# import math
# radius_circle=float(input("Enter radius of circle: "))
# area= math.pi * radius_circle ** 2
# print(f"The area of the circle is {area:.2f}")


# next
# length=float(input("Enter the length of the rectangle: "))
# width=float(input("Enter the width of the rectangle: "))
# area=length*width
# perimeter=2 * (length+width)
# print(f"The perimeter is {perimeter} \nThe area is {area}")
# print(f"Thank you for using our service!")

# next
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))
# total=num1+num2+num3
# product= num1 * num2 * num3
# average=total/3
# print(f"The sum is {total} \nThe product is {product} \nThe average is {average}")
#

# next
# talents=float(input("Enter talents: "))
# pounds=float(input("Enter pounds: "))
# lots=float(input("Enter lots: "))
# total_lots= talents * 20 * 32 + pounds * 32 + lots
# total_grams= total_lots * 13.3
# total_kilograms= int(total_grams // 1000)
# grams=total_grams % 1000


# next
# length=float(input("Enter the length of a zander in cm: "))
# if length < 42:
#     left=  42 - length
#     print(f"The Zander does not fulfill the size limit"
#           f"\nRelease the fish back into the lake \nThe fish was {left} cm below the size limit.")
# else:
#     print("The zander fulfill the size limit")
#

# next
# cabin=input("Enter cabin class: ").upper()
# if cabin == "LUX":
#     print("upper-deck cabin with a balcony.")
# elif cabin == "A":
#     print("above the car deck, equipped with a window.")
# elif cabin == "B":
#     print("windowless cabin above the car deck.")
# elif cabin == "C":
#     print("windowless cabin below the car deck.")
# else:
#     print("Invalid cabin class")


# next
# gender=input("Enter biological gender(female-male): ")
# hemoglobin=int(input("Enter hemoglobin value(g/l): "))
# if gender == "female":
#     if hemoglobin < 117:
#         print("You hemoglobin is low")
#     elif hemoglobin > 155:
#         print("Your hemoglobin is too high")
#     else:
#         print("You hemoglobin is normal")
# if gender == "male":
#     if hemoglobin < 134:
#         print("You hemoglobin is low")
#     elif hemoglobin > 167:
#         print("Your hemoglobin is too high")
#     else:
#         print("You hemoglobin is normal")


# next
# count=1
# while count <= 1000:
#     if count % 3 == 0:
#         print(count)
#     count+=1

# next

# inches= float(input("Enter inches: "))
# while inches >=0:
#     cm= inches * 2.54
#     print(f"Centimeters: {cm}")
#     inches = float(input("Enter inches: "))
# print("Program ended")


# next
# smallest=None
# largest=None
# while True:
#     user_input = input("Enter a number (empty to quit): ")
#     if user_input == '':
#         break
#     number=float(user_input)
#     if smallest is None or number < smallest:
#         smallest= number
#     if largest is None or number > largest:
#         largest=number
# print("smallest is ",smallest)
# print("largest is ",largest)


# next
# import random
# print("Welcome to guessing game!")
# lower=1
# upper=10
# number=random.randint(1,10)
# user=int(input("Guess the number: "))
# while user != number:
#     if user > number:
#         print("Too high")
#     else:
#         print("Too low")
#     user = int(input("Guess the number: "))
# print("Correct")

# next
# correct_user= "python"
# correct_password= "rules"
# count=0
#
# while count < 5:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == correct_user and password == correct_password:
#         print("Welcome")
#         break
#     else:
#         count+=1
# if count == 5:
#     print("Access denied")

# next
# import random
# user=int(input("How many dice to roll: "))
# total=0
# for i in range(user):
#     roll = random.randint(1,6)
#     total += roll
# print(f"The sum of the dice is: {total}")

# next
# numbers=[]
# user_input = input("Enter a number (empty to quit): ")
# while user_input != '':
#     numbers.append(int(user_input))
#     user_input = input("Enter a number (empty to quit): ")
# numbers.sort(reverse=True)
# top_five= numbers[:5]
#
# for n in top_five:
#     print(n)

# next
# cities = []
#
# for a in range(5):
#     cities.append(input("Enter the name of a city: "))
# for city in cities:
#     print(city)


# next
# def gasoline(gal):
#     liters= gal * 3.78
#     return liters
# user=float(input("Enter the volume in gallons: "))
# while user >=0:
#     result=gasoline(user)
#     print(f"{result:.2f} liters.")
#     user = float(input("Enter the volume in gallons: "))
# print("Program ended")

# next
# import math
# def pizza(diameter,price):
#     radius= diameter /2
#     area= math.pi * radius **2
#     area_square_m= area /10000
#     unit_price = price /area_square_m
#     return unit_price
# diameter_pizza1=float(input("Enter diameter of first pizza: "))
# price_pizza1=float(input("Enter price of first pizza: "))
# diameter_pizza2=float(input("Enter diameter of second pizza: "))
# price_pizza2=float(input("Enter price of second pizza: "))
# pizza1=pizza(diameter_pizza1,price_pizza1)
# pizza2=pizza(diameter_pizza2,price_pizza2)
# if pizza1 > pizza2:
#     print(f"The second pizza provides better value for the money")
# else:
#     print(f"The first pizza provides better value for money")
#
# num1= int(input("Enter first integer: "))
# num2= int(input("Enter the second integer: "))
# num3= int(input("Enter the third integer: "))
# sum_of_numbers= num1 + num2 + num3
# product_of_numbers= num1 * num2 * num3
# average_of_numbers= sum_of_numbers / 3
# print(f"The sum of the numbers: {sum_of_numbers} \nThe product of the numbers: {product_of_numbers} \nThe average of the numbers: {average_of_numbers}")

#
# talents=float(input("Enter talents: "))
# pounds=float(input("Enter pounds: "))
# lots=float(input("Enter lots: "))
# total_grams= talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3
# kilograms= total_grams // 1000
# remaining_grams= total_grams % 1000
# print(f"The weight in modern units: {int(kilograms)} kilograms and {remaining_grams:.2f} grams.")
#

# import random
#
# a=random.randint(0,9)
# b=random.randint(0,9)
# c=random.randint(0,9)
#
# code1=str(a) + str(b) + str(c)
# print(f"3-digit code: {code1}")
#
# d=random.randint(1,6)
# e=random.randint(1,6)
# f=random.randint(1,6)
# g=random.randint(1,6)
#
# code2=str(d) + str(e) + str(f) + str(g)
# print(f"4-digit code: {code1}")
#
# import random
#
# a= random.randint(0,9)
# b= random.randint(0,9)
# c= random.randint(0,9)
#
# code3 = str(a)+str(b)+str(c)
# print("3-digit code:", code3)
#
# d= random.randint(1,6)
# e= random.randint(1,6)
# f= random.randint(1,6)
# g= random.randint(1,6)
#
# code4 = str(d)+str(e)+str(f)+str(g)
# print("4-digit code:", code4)


# def gallons_to_liters (gal):
#     litres=gal * 3.785
#     return litres
# user=float(input("Enter a volume in American gallons (negative value to quit): "))
# while user >=0:
#     result=gallons_to_liters(user)
#     print(f"{user} American gallons is {result:.2f} liters.")
#     user = float(input("Enter a volume in American gallons (negative value to quit): "))
# print("Program finished.")



# def get_season(month):
#     if month == 12 or month == 1 or month == 2:
#         return "winter"
#     elif month == 3 or month == 4 or month == 5:
#         return "spring"
#     elif month == 6 or month == 7 or month == 8:
#         return "summer"
#     elif month == 9 or month == 10 or month == 11:
#         return "autumn"
#
# user=int(input("Enter the number of a month (1-12): "))
# print(f"You entered {user}")
# if user < 1 or user > 12:
#     print("Please enter a number between 1 and 12.")
# else:
#     result=get_season(user)
#     print(f"The season is {result}.")

# names=set()
# user=input("Enter a name (empty to quit): ")
# while user != '':
#     if user not in names:
#         names.add(user)
#         print("New name")
#     else:
#         print("Existing name")
#     user = input("Enter a name (empty to quit): ")
# for i in names:
#     print(names)




airports={}
user= int(input("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit "
                "\nPlease choose an option (1-3): "))
while user != 3:
    if user ==1:
        code=input("Enter the ICAO code: ").upper()
        name=input("Enter the airport name: ").title()
        airports[code]=name
        print(f"Airport {name} with ICAO code {code} has been added.")

    elif user == 2:
        code=input("Enter the ICAO code: ").upper()
        if code in airports:
            print(f"The airport with ICAO code {code} is {airports[code]}.")
        else:
            print(f"No airport found with ICAO code {code}.")
    else:
        print("Invalid option")
    user = int(input("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit "
                     "\nPlease choose an option (1-3): "))

print("Thank you for using the Airport Data Management system. Goodbye!")









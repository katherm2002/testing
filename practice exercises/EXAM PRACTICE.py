# EXERCISE 1
# first_name=input("Enter your first name: ")
# last_name=input("Enter your last name: ")
# print(f"Hello, {first_name.title()} {last_name.title()} !")
#

# Exercise 2
# import math
# radius_of_circle=float(input("Enter the radius of a circle: "))
# area = math.pi *radius_of_circle**2
# print(f"The area of the circle is {area}.")

# Exercise 3
# user_age=int(input("Enter your age: "))
# if user_age >= 18:
#     print("You are allowed to vote")
# else:
#     years_left=18-user_age
#     print(f"You are {years_left} year left to vote")

# Exercise 4
# inches=float(input("Enter inches: "))
#
# while inches >=0:
#     cm = inches * 2.54
#     print(f"{cm} centimeters")
#     inches=float(input("Enter inches: "))
# print("program ended")


# Exercise 5
# import random
# number=random.randint(1,10)
# user_number=int(input("Guess the number: "))
# while True:
#     if user_number < number:
#         print("The number is too low")
#     elif user_number > number:
#         print("The number is too high")
#     elif user_number == number:
#         print("The number is correct!!")
#         break
#     user_number = int(input("Guess the number: "))

# Exercise 6 study again because i ask something to chat gpt during
# import random
# user_rolls=int(input("How many dice do you want to roll?: "))
# total=0
# for i in range(user_rolls):
#         roll=random.randint(1,6)
#         total+=roll
# print(total)

# Exercise 7 study again because i ask something to chat gpt during
# numbers=[]
# user_number=input("Enter number (empty to quit): ")
# while user_number != "":
#     numbers.append(int(user_number))
#     user_number = input("Enter number (empty to quit): ")
# print("Smallest number:", min(numbers))
# print("Largest number:", max(numbers))


# Exercise 8 no tengo idea de como hacerlo
# user_number=int(input("Enter a number: "))


# Exercise 9
# def distance(km):
#     return km * 0.621371
# distance_km = float(input("Enter km: "))
# while distance_km >= 0:
#     result=distance(distance_km)
#     print(result)
#     distance_km = float(input("Enter km: "))
# print(f"Enter a positive number")

# Exercise 10
# def numbers(lst):
#     even_numbers=[]
#     for i in lst:
#         if i % 2 ==0:
#             even_numbers.append(i)
#     return even_numbers
# number=[1,2,3,4,5,6,7,8,9,12,13,54]
# result=numbers(number)
# print(f"The original list is {number}")
# print(f"The new list is {result}")

# Exercise 11 bonus
# import math
# def pizza(diameter, price):
#     radius=diameter/2
#     area_cm2=math.pi * radius ** 2
#     area_m2=area_cm2*10000
#     unit_price_per_square_meter=price*area_m2
#     return unit_price_per_square_meter
# diameter1=float(input("Enter the diameter of the first pizza: "))
# price1=float(input("Enter the price of the first pizza: "))
# diameter2=float(input("Enter the diameter of the second pizza: "))
# price2=float(input("Enter the price of the second pizza: "))
# result1=pizza(diameter1,price1)
# result2=pizza(diameter2,price2)
# if result1 > result2:
#     print(f"The second pizza gives better value for money")
# else:
#     print(f"The first pizza gives better value for money")


# MODULE2
# import math
# radius_circle=float(input("Enter the radius of a circle: "))
# side_length_square=float(input("Enter the side length of a square: "))
# area_circle=math.pi*radius_circle**2
# area_square=side_length_square**2
# print(f"The area of the circle is {area_circle} and the area of the square is {area_square}")
#

# next
# banana=float(input("Enter the amount of banana in kg: "))
# apple=float(input("Enter the amount of apple in kg: "))
# orange=float(input("Enter the amount of orange in kg: "))
# banana_price= banana * 2.85
# apple_price= apple * 3.15
# orange_price = orange * 4.05
# total= banana_price + apple_price + orange_price
# print(f"Bananas: €{banana_price}")
# print(f"Apples: €{apple_price}")
# print(f"Oranges: €{orange_price}")
# print(f"Total: €{total}")


# next
# import random
# six_sided=random.randint(1,6)
# twenty_sided=random.randint(1,20)
# total=six_sided+twenty_sided
# print(six_sided)
# print(twenty_sided)
# print(total)


# module3
# user_age=int(input("Enter your age: "))
# if user_age < 18:
#     years_left= 18- user_age
#     print(f"You can vote in {years_left} years")
# else:
#     print(f"You can vote!")

# next
# consumption=float(input("Enter your electricity consumption in kWh: "))
# if consumption <= 50:
#     price= consumption * 0.10
# elif consumption <= 200:
#     price= 50 * 0.10 + (consumption - 50) * 0.08
# else:
#     price= 50 * 0.10 + 150 * 0.08 + (consumption -200) *0.06
# print(f"Electricity bill: €{price:.2f}")


# next
# physics=int(input("Enter your score in physics: "))
# mathematics=int(input("Enter your score in mathematics: "))
# chemistry=int(input("Enter your score in chemistry: "))
# if physics < 50 or mathematics < 50 or chemistry < 50:
#     print("You cannot receive a scholarship")
# elif physics > 90 and mathematics > 90 or chemistry > 95:
#     print("You can receive a scholarship, congratulations!")
# else:
#     print("You cannot receive a scholarship")

# module 5 while

# user_number = int(input("Enter a positive integer: "))
# if user_number <= 0:
#     print("Error: please enter a positive integer.")
# else:
#     i = 0
#     while i <= user_number:
#         print(i)
#         i += 2

# same as last
# user_number = int(input("Enter a positive integer: "))
# if user_number <= 0:
#     print("error")
# else:
#     count=0
#     while count <= user_number:
#         print(count)
#         count+=2


# sum=0
# count=0
# while sum<= 1000:
#     user_number = int(input("Enter a positive integer: "))
#     sum+= user_number
#     count+=1
# print(f"The final sum is {sum}")
# print(f"You entered {count} numbers")


# sum=0
# count=0
# while sum <= 500:
#     user_input=int(input("Enter a positive number: "))
#     sum+=user_input
#     count+=1
# print(f"The final sum is {sum}")
# print(f"you entered {count} numbers")

# next
# initial_height=float(input("Enter the initial height in m: "))
# time=0
# current_height= initial_height
# while current_height > 0:
#     time+=1
#     fallen_distance=s =0.5 * 9.81 * time **2
#     current_height= initial_height - fallen_distance
#     print(f"After {time} seconds, height is {current_height:.2f} meters")
# print(f"The object took {time} to fall")

#
# initial_acceleration = float(input("Enter acceleration of the car in m/s2: "))
#
# time = 0
# distance = 0
#
# while distance < 100:
#     time += 1
#     distance = 0.5 * initial_acceleration * time ** 2
#     print(f"The current distance travelled is {distance:.2f} meters")
#
# print(f"The total time is {time} seconds")

# module5
# user_number=int(input("Enter a number: "))
# if user_number <=0:
#     print("Error")
# else:
#     for i in range(0, user_number +1):
#         if i % 2 == 0:
#             print(i)


# next
# numbers = []
#
# user_number = input("Enter a number (empty to quit): ")
#
# while user_number != "":
#     numbers.append(int(user_number))
#     user_number = input("Enter a number (empty to quit): ")
#
# unique_numbers = []
#
# for i in numbers:
#     if i > 100 and i not in unique_numbers:
#         unique_numbers.append(i)
#
# for num in unique_numbers:
#     print(num)











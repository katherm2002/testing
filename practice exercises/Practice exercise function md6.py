# def greet(times):
#     for i in range(times):
#         print("Round " + str(i+1) + " of saying hello.")
#     return
#
# print("A new day starts with greetings.")
# greet(5)
# print("Let's greet some more.")
# greet(2)

# EXERCISE 1 HOMEWORK
# import random
# def dice():
#     return random.randint(1,6)
# roll=dice()
#
# while roll !=6:
#     print(roll)
#     roll=dice()
# print(roll)

# EXERCISE1.1 AI
# def number(a):
#     return a*2
#
# num=int(input("Enter a number: "))
# result=number(num)
# print(result)

# EXERCISE 1.2 AI
# def mayor_integer(a,b):
#     if a>b:
#         return a
#     if b>a:
#         return b
# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# result=mayor_integer(num1,num2)
# print(f"The greater number is {result}")

# EXERCISE 3.1 AI
# import random
# def number(a,b):
#     return random.randint(a,b)
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# result=number(num1,num2)
# print(result)

# Exercise 3.2 ai
# import random
# def number(n):
#     return random.randint(1,n)
# user_number=int(input("Enter a number: "))
# result=number(user_number)
# while result!= user_number:
#     print(result)
#     result=number(user_number)
# print(result)

# EXERCISE 4.1 AI
# def centimeters_to_meters(cm):
#     return cm*0.01
# user_cm=float(input("Enter cm: (negative to quit): "))
# while user_cm>=0:
#     meters=centimeters_to_meters(user_cm)
#     print(meters)
#     user_cm = float(input("Enter cm: (negative to quit): "))

# EXERCISE 3 HOMEWORK
# def gasoline(gal):
#     return gal * 3.78541178
# value=float(input("Enter the volume in gallons: "))
# while value>=0:
#     litres=gasoline(value)
#     print(litres)
#     value=float(input("Enter the volume in gallons: "))

# EXERCISE 5.1 AI
# def sum_list(lst):
#     total = 0
#     for n in lst:
#         total += n
#     return total
# numbers=[2,4,6]
# result=sum_list(numbers)
# print(result)


# EXERCISE 4 HOMEWORK
# def sum_numbers(lst):
#     total=0
#     for i in lst:
#         total += i
#     return total
# numbers=[2,8,10,25]
# result=sum_numbers(numbers)
# print(result)

# EXERCISE 6.1 AI
# def only_even(numbers):
#     even_numbers=[]
#     for n in numbers:
#         if n % 2 ==0:
#             even_numbers.append(n)
#     return even_numbers
# numbers= [1,2,3,4,5,6,7,8]
# result=only_even(numbers)
# print(f"The original list is {numbers}")
# print(f"Even numbers {result}")

# EXERCISE 5 HOMEWORK
# def only_even(numbers):
#     even_numbers=[]
#     for n in numbers:
#         if n % 2 ==0:
#             even_numbers.append(n)
#     return even_numbers
# numbers=[10,11,12,13,14,15,16,17,18,19,20]
# result=only_even(numbers)
# print(f"The original list is {numbers}")
# print(f"Even numbers {result}")


# CLASS 6
# def beautiful_day ():
#     print("Today is a sunny day")
#     return
# beautiful_day()

# def addition(a,b):
#     return a+b
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# result=addition(num1,num2)
# print(f"The sum is {result}")

# NEW EXAMPLE
# def change():
#     city= "vantaa"
#     print(f"The city is {city}")
#     return
# city= "Helsinki"
# print(f"The city in the beginning of the program is {city}")
# change()
# print(f"The city at the end of the program is {city}")

#
# def gasoline(gal):
#     return gal * 3.78541178
# value=float(input("Enter the volume in gallons: "))
# while value>=0:
#     litres=gasoline(value)
#     print(litres)
#     value=float(input("Enter the volume in gallons: "))



# def area_rectangle(a,b):
#     return a*b
# length=float(input("Enter the length of a rectangle: "))
# width=float(input("Enter the width of a rectangle:"))
# result=area_rectangle(length,width)
# print(result)
#
# def area_circle(a):
#     return 3.149 * a**2
# radius_of_circle=float(input("Enter the radius of circle: "))
# result=area_circle(radius_of_circle)
# print(result)
#
# def temperature(a):
#     return (a * 9/5) +32
# celsius=float(input("Enter temperature in celsius: "))
# result=temperature(celsius)
# print(result)



# NOT READY
# def greet(greeting,times):
#     for i in range(times):
#         print(greeting + "Round " + str(i+1))
#     return
# print("This is an example of user defined function with for loop")
# greeting=(input("Enter a greeting: "))
# while True:
#     if greeting=="done":
#         break
# times=int(input("Enter times: "))
# greet(greeting,times)
# greeting = (input("Enter a greeting: "))
# print("it´s done")


# LIST EXAMPLES
# def inventory(items):
#     print("You have the following items:")
#     for item in items:
#         print("- " + item)
#     return
# backpack = ["Water bottle", "Map", "Compass"]
# inventory(backpack)
# backpack.append("Swiss Army knife")
# inventory(backpack)


# exercise class
































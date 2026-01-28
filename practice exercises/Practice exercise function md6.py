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










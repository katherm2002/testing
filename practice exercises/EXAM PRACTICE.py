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

# numbers=[]
# user_number = input("Enter a number (empty to quit): ")
# while user_number != '':
#     numbers.append(int(user_number))
#     user_number = input("Enter a number (empty to quit): ")
# positive=0
# negative=0
# zeros=0
# for i in numbers:
#     if i >0:
#         positive+=1
#     elif i<0:
#         negative +=1
#     else:
#         zeros +=1
# print(f"Positive numbers: {positive}")
# print(f"Negative numbers: {negative}")
# print(f"Zeros: {zeros}")


# words=[]
# user_words = input("Enter a word (empty to quit): ")
# while user_words != '':
#     words.append(user_words)
#     user_words = input("Enter a word (empty to quit): ")
# unique_list=[]
# for i in words:
#     if i not in unique_list:
#         unique_list.append(i)
#
# for n in unique_list:
#     print(n)



# exam_scores=[]
# student_number=int(input("Enter how many students there are: "))
# for i in range(student_number):
#     scores = int(input("Enter exam scores: "))
#     exam_scores.append(scores)
# average= sum(exam_scores)/student_number
# highest=max(exam_scores)
# lowest=min(exam_scores)
# count_90=0
# for score in exam_scores:
#     if score >= 90:
#         count_90 +=1
# print(f"Average score: {average}")
# print(f"Highest score: {highest}")
# print(f"Lowest score: {lowest}")
# print(f"Scores >= 90: {count_90}")


# number=int(input("Enter a integer: "))
# count=0
# for i in range(1,10+1):
#     print(f"{number} x {i} = {number * i}")


# numbers=[]
# n=input("Enter a integer 'empty to quit': ")
# while n != '':
#     numbers.append(int(n))
#     n = input("Enter a integer 'empty to quit': ")
# if len(numbers)<2:
#     print("You must enter at least two numbers")
# else:
#     numbers.sort()
#     second_largest = numbers[-2]
#     print(f"The second largest number is {second_largest}")


# numbers = []
#
# n = input("Enter an integer (empty to quit): ")
# while n != "":
#     numbers.append(int(n))
#     n = input("Enter an integer (empty to quit): ")
#
# unique_numbers = []
# for i in numbers:
#     if i not in unique_numbers:
#         unique_numbers.append(i)
#
# max_count = 0
# most_frequent = None
#
# for num in unique_numbers:
#     count = numbers.count(num)
#     print(f"{num} appears {count} times")
#
#     if count > max_count or (count == max_count and (most_frequent is None or num < most_frequent)):
#         max_count = count
#         most_frequent = num
#
# print(f"Most frequent: {most_frequent}")


# EXAM PRACTICE 2
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# print(f"Hello {name.title()}, You are {age} years old.")

# exercise 2
# length=float(input("Enter the length of a rectangle: "))
# width=float(input("Enter the width of a rectangle: "))
# area=length*width
# perimeter=2 *(length+width)
# print(f"The area is: {area} and the perimeter is {perimeter}")

# exercise 3
# number=int(input("Enter a number: "))
# if number % 2 ==0:
#     print(f"{number} is even number.")
# else:
#     print("Odd number")

# exercise 4
# count=0
# sum=0
# number = input("Enter a number 'empty to quit': ")
# while number != '':
#     sum+=int(number)
#     number = input("Enter a number 'empty to quit': ")
#     count+=1
# print(f"The sum of the numbers is {sum}")
# print(f"you entered {count} numbers")

# exercise 5
# n=int(input("Enter a number: "))
# if n<=0:
#     print("Error")
# else:
#     x=0
#     while x <=n:
#         print(x)
#         x+=5

# exercise 6
# n=int(input("Enter a number: "))
# for i in range(1,10+1):
#     print(f"{n} x {i} = {n*i}")


# exercise 7
# temp=[]
# times=int(input("How many temperatures you want to enter: "))
# for i in range(times):
#     temperature=float(input("Enter temperature: "))
#     temp.append(temperature)
# average=sum (temp) / times
# print(f"The average temperature is {average}")
# print(f"The highest temperature is {max(temp)}")
# print(f"The lowest temperature is {min(temp)}")

# exercise 8
# numbers = []
# x = input("Enter an integer (empty to quit): ")
#
# while x != "":
#     numbers.append(int(x))
#     x = input("Enter an integer (empty to quit): ")
#
# unique = []
# for n in numbers:
#     if n not in unique:
#         unique.append(n)
#
# for n in unique:
#     print(f"{n} appears {numbers.count(n)} times")

# exercise 9
# def to_seconds(minutes):
#     return minutes*60
# m=float(input("Enter minutes: "))
# while m>=0:
#     print(to_seconds(m))
#     m = float(input("Enter minutes: "))
# print("program ended")

# exercise 10
# def largest(lst):
#     return max(lst)
# numbers=[1,2,3,4,5,6,7,8,9]
# result=largest(numbers)
# print(result)





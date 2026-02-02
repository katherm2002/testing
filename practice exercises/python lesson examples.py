# import math
# radius_circle=float(input("Enter the radius of a circle: "))
# side_length_square=float(input("Enter the side length of a square: "))
# area_circle=math.pi * radius_circle ** 2
# area_square= side_length_square**2
# print(f"The area of the circle is {area_circle}")
# print(f"The area of the square is {area_square}")
#

# banana=float(input("Enter the amount of banana in kg: "))
# apple=float(input("Enter the amount of apple in kg: "))
# orange=float(input("Enter the amount of orange in kg: "))
# price_banana=banana*2.85
# price_apple=apple*3.15
# price_orange=orange*4.05
# total=price_banana+price_apple+price_orange
# print(f"Shopping summary: \nBananas: €{price_banana:.2f} \nApples: €{price_apple:.2f}  \nOranges: €{price_orange:.2f}")
# print(f"Total: €{total:.2f} ")

# import random
# six_sided=random.randint(1,6)
# twenty_sided=random.randint(1,20)
# total=six_sided + twenty_sided
# print(f"The first roll is: {six_sided} \nThe second roll is: {twenty_sided}")
# print(f"The sum is {total}")

# age=int(input("Enter your age: "))
# if age < 18:
#     years_left= 18 - age
#     print(f"You can vote in {years_left} years")
# else:
#     print(f"Congratulations, You can vote!")

# n=int(input("Enter a number: "))
# if n <=0:
#     print("Error")
# else:
#     for x in range(0,n+1,2):
#         print(x)
#

# count=0
# total=0
# while total < 1000:
#     n = int(input("Enter a number: "))
#     total+=n
#     count+=1
# print(f"The final sum is {total}")
# print(f"You entered {count} numbers")


# initial_height=float(input("Enter the initial height of the object in m: "))
# current_height=initial_height
# time=0
# while current_height>0:
#     time += 1
#     s=0.5 * 9.81 * time**2
#     current_height=initial_height - s
#     print(f"After {time} seconds, height is {current_height:.2f} meters")
# print(f"The object took {time} seconds to fall")



# n=int(input("Enter a number: "))
# if n<=0:
#     print("Error")
# else:
#     for i in range(0,n+1,2):
#         print(i)


# numbers=[]
# n=input("Enter a number 'empty to quit': ")
# while n!='':
#     numbers.append(int(n))
#     n = input("Enter a number 'empty to quit': ")
# unique_numbers=[]
# for i in numbers:
#     if i not in unique_numbers:
#         unique_numbers.append(i)
# for x in unique_numbers:
#     if x > 100:
#         print(x)


# def total(a,b):
#     return a+b
# result=total(2,6)
# print(result)

# def names(lst):
#     new_list=[]
#     for i in lst:
#         if len(i)> 5:
#             new_list.append(i)
#     return new_list
# animals_names=["cat","dog","elephant","lion","giraffe"]
# result=names(animals_names)
# print(f"The original list is {animals_names}.")
# print(f"The new list is {result}.")
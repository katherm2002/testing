#Task:
# Write a program that asks the user to enter integers until they input an empty string to quit. Store the numbers in a list.
# After input ends, the program prints:
    # how many numbers were positive
    # how many were negative
    # how many were zeros

# Tip: Use a while loop for input, then a for loop to count.

# numbers=[]
# n=input("Enter a number 'empty to quit': ")
# while n!= '':
#     numbers.append(int(n))
#     n = input("Enter a number 'empty to quit': ")
# positives=0
# negatives=0
# zeros=0
# for i in numbers:
#     if i > 0:
#         positives+=1
#     elif i < 0:
#         negatives+=1
#     else:
#         zeros+=1
# print(f"{positives} are positives")
# print(f"{negatives} are negatives")
# print(f"{zeros} are zeros")


# Exercise 2. Remove duplicates (keep original order)

# Task:
# Write a program that asks the user to enter words until they input an empty string to quit. Store the words in a list.
# Then create a new list that contains each word only once in the same order they were first entered.
# Finally print the new list, one word per line.

# Tip: You can check if word not in unique_list: before adding.

# words=[]
# user=input("Enter a word 'empty to quit': ")
# while user != '':
#     words.append(user)
#     user = input("Enter a word 'empty to quit': ")
# unique_list=[]
# for i in words:
#     if i not in unique_list:
#         unique_list.append(i)
# for x in unique_list:
#     print (x)


# Exercise 3. Grade statistics

#Task:
# Write a program that asks the user how many students there are. Then ask the user to enter that many exam scores (integers from 0 to 100). Store them in a list.
# At the end, print:
    # the average score (as a float, e.g. 72.4)
    # the highest score
    # the lowest score
    # how many scores are >= 90

#Tip: Use a for loop to read scores. You can use sum(list), max(list), and min(list).
# exam_scores=[]
# amount=int(input("How many students there are?: "))
# for i in range(amount):
#     scores=int(input("Enter exam scores: "))
#     exam_scores.append(scores)
# average= sum(exam_scores) / amount
# count=0
# for a in exam_scores:
#     if a >= 90:
#         count+=1
# print(f"The average score is {average:.1f}")
# print(f"The highest score is {max(exam_scores)}")
# print(f"The lowest score is {min(exam_scores)}")
# print(f"scores >=90 : {count} ")



# Exercise 4. Multiplication table row

# Task:
# Write a program that asks the user for an integer n.
# Print the multiplication row for n from 1 to 10, like this (example if n = 7):
    # 7 x 1 = 7
    # 7 x 2 = 14
    # ...
    # 7 x 10 = 70

# Tip: Use a for loop from 1 to 10.

# n=int(input("Enter a number: "))
# for i in range(1,10):
#     print(f"{n} X {i} = {n*i}")


# Exercise 5. Find the second largest number

# Task:
# Write a program that asks the user to enter at least two integers (keep asking until they do). The user ends input with an empty string. Store the numbers in a list.
# Then print the second largest number.

# Tip: One simple way: sort the list and look at the second last item.
# Extra tip: think about what happens if the largest number appears multiple times—do you want “second largest” to be different,
# or is it okay if it’s the same? (Pick one and implement it.)

# numbers=[]
# n=input("Enter a number 'empty to quit': ")
# while n != '':
#     numbers.append(int(n))
#     n = input("Enter a number 'empty to quit': ")
# if len(numbers) < 2:
#     print("Error")
# else:
#     numbers.sort()
#     print(f"The second largest number is {numbers[-2]}")
#


# BONUS Most frequent number

# This one's more difficult! Great practice though.

# Task:
# Write a program that asks the user to enter integers until they input an empty string to quit. Store them in a list.
# Then print:
    # each unique number and how many times it appears
    # the most frequent number (if there’s a tie, print the smallest number)

# Example:
# Input: 5, 2, 5, 7, 2, 5
# Output:
    # 2 appears 2 times
    # 5 appears 3 times
    # 7 appears 1 time
    # Most frequent: 5

# numbers=[]
# n=input("Enter a number 'empty to quit': ")
# while n!='':
#     numbers.append(int(n))
#     n = input("Enter a number 'empty to quit': ")
# unique_numbers=[]
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
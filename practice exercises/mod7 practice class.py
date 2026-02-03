# Exercise 1
# fruits={}
# for i in range(3):
#     name= input("Enter fruit name: ")
#     amount=float(input("Enter amount in kg: "))
#     fruits[name]= amount
# print(fruits)

# Exercise 2
# numbers=[]
# n=int(input("Enter a number (enter 0 to stop): "))
# while n != 0:
#     numbers.append(n)
#     n = int(input("Enter a number (enter 0 to stop): "))
#
# unique_numbers= set(numbers)
# print(unique_numbers)

# different method  exercise 2
# numbers_list=[]
# numbers_set=set()
# n=int(input("Enter a number (enter 0 to stop): "))
# while n!= 0:
#     numbers_list.append(n)
#     n = int(input("Enter a number (enter 0 to stop): "))
# for num in numbers_list:
#     numbers_set.add(num)
# print(numbers_set)


# Exercise 3
# phonebook={}
# while True:
#     user = input("What do you want to do (add, search or quit): ")
#
#     if user == 'add':
#         name=input("Enter contact name: ")
#         phone_number=int(input("Enter phone number: "))
#         phonebook[name]=phone_number
#     elif user == 'search':
#         search_name=input("Enter name: ")
#         if search_name in phonebook:
#             print(f"{search_name}'s phone number is {phonebook[search_name]}.")
#         else:
#             print("Contact not found")
#     elif user == 'quit':
#         print("Program ended")
#         break
#     else:
#         print("Invalid input")


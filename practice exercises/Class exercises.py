
# rounds= int(input("How many rounds would you like? "))
# finished_rounds= 0
# while finished_rounds < rounds:
#     print("Good morning")
#     finished_rounds = finished_rounds + 1

# number = int(input("Enter an integer number: "))
# finished_number = 1
#
# while finished_number <= number:
#     print(finished_number)
#     finished_number += 1

# number=int(input("Enter a number: "))
# finished_number= 0
#
# while finished_number<=number:
#         print(finished_number)
#         finished_number+=2

# amount= int(input("How many numbers do you want to sum?"))
# count=0
# total_sum=0
# while count<amount:
#         number=int(input("Enter a number:"))
#         total_sum=total_sum+number
#         count=count +1
# print("Total sum:",total_sum)


# count=0
# total_sum=0
# while total_sum <=1000:
#         number=int(input("Enter a number"))
#         total_sum=total_sum+number
#         count=count+1
# print("Final sum:", total_sum)
# print("Numbers entered:", count)









# PASSWORD EXERCISE
# password= ""
# while password != "Python123":
#     password = str(input("Enter your password: "))
#     print("Incorrect password, try again")
# print("Correct password")


# Example 3
# import random
# dice1 = dice2 = rolls = 0
# while (dice1!=6 or dice2!=6):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     rolls = rolls + 1
# print(f"Rolled {rolls:d} times.")

# number= 0
# while number >= 0:
#     number = int(input("Enter a positive integer: "))
#     print("Error, please enter a positive integer")
# print(number)

# Nested loops
# first = 1
# while first <= 5:
#     second = 1
#     while second <= 5:
#         print(f"{first} times {second} is {first*second:d}")
#         second = second + 1
#     first = first + 1

# import random
# rounds= 0
# total_rolls = 0
#
# while rounds < 100000:
#     dice1 = dice2 = rolls = 0
#     while (dice1!=6 or dice2!=6):
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)
#     rolls = rolls +1
#     rounds = rounds +1
#     total_rolls = total_rolls + rolls
#
# average_rolls=total_rolls + rolls

# BOOK EXERCISES
# name= "Eric"
# message ="would you like to learn some Python today?"
# print("Hello", name, message)


# name= "Eden"
# print(name.upper())
# print(name.lower())
# print(name.title())

# magicians=("alice","bob","charlie")
# for magician in magicians:
#     print(magician.title()+",that was a great trick!")
#     print("I can't wait to see your next trick," + magician.title()+ ".\n")
# print("Thank you, everyone.")

# pizzas=("pepperoni","tuna","kana")
# for pizza in pizzas:
#     print("I like "+pizza+" pizza.")
# print("I really love pizza")

# animals=("dog","cat","hamster")
# for animal in animals:
#     print("A", animal, "would make a great pet")
# print("Any of this animals would make a great pet")

# players=["charles","martina","michael","florence","eli"]
# print("The last players are:")
#
# for player in players[3:]:
#     print(player.title())


# pizzas=["pepperoni","tuna","chicken","kebab"]
# friend_pizzas=pizzas[:]
#
# pizzas.append('tofu')
# friend_pizzas.append('corn')
# print("My favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza)
# print("My friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza)


# answer=int(input("enter your answer: "))
# if answer != 42:
#     print("That is not the correct answer.")


# banned_users= ["elsa","camila","felipe"]
# user_name=input("enter your name: ")
# if user_name not in banned_users:
#     print(user_name.title()+", you can post a response if you wish")
# else:
#     print(user_name.title()+" you are banned")


# age= int(input("Please enter your age: "))
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("You can't vote!")



# age=int(input("Enter your age "))
# if age<4:
#     price=0
# elif age < 18:
#     price=5
# else:
#     price=10
# print("Your admission cost is €" + str(price) + ".")


# alien_color = "red"
# if alien_color == "green":
#         print("you just earned 5 points")
# elif alien_color == "yellow":
#         print("You just earned 10 points")
# else :
#         print("You just earned 15 points")


# age=int(input("Enter your age "))
# if age <2:
#         print("The person is a baby")
# elif age<4:
#         print("The person is a toddler")
# elif age<13:
#         print("The person is a kid")
# elif age<20:
#         print("The person is an teenager")
# elif age<65:
#         print("The person is an adult")
# else:
#         print("You are an elder")


# person0={'first_name':'Alip', 'Last_name': 'Tursun','age':'26', 'city': 'Helsinki'}
# print(person0['first_name'])
# print(person0['Last_name'])
# print(person0['age'])
# print(person0['city'])


# DICTIONARY
# favorite_numbers={'kathy':'7','Alip':'8','Diana':'3','Elena':'2'}
# nim=favorite_numbers['kathy']
# print(f"Kathy's favorite number is {nim}")
# favorite_numbers['Alip']
# print(f"Alip's favorite number is {favorite_numbers['Alip']}")
# favorite_numbers['Diana']
# print(f"Diana's favorite number is {favorite_numbers['Diana']}")
# favorite_numbers['Elena']
# print(f"Elena favorite number is {favorite_numbers['Elena']}")


# user_0={
#         'username': 'kamuvar',
#         'first':'kathy',
#         'last':'musikka'}
# for key, value in user_0.items():
#         print("\nKey: " + key)
#         print("Value: " + value)


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
#
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
#


# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'kuskokwim': 'alaska',
#     'yangtze': 'china',
#     }
#
# for river, country in rivers.items():
#     print(f"The {river.title()} flows through {country.title()}.")
#
# print("\nThe following rivers are included in this data set:")
# for river in rivers.keys():
#     print(f"- {river.title()}")
#
# print("\nThe following countries are included in this data set")
# for country in rivers.values():
#         print(f"-{country.title()}")


# car=input("What kind of rental car you would like? ")
# print(f"Let me see if i can find you a {car}.")

# answer=int(input("How many people are in your dinner group? "))
# if answer > 8:
#         print("You'll have to wait for a table.")
# else:
#         print("Your table is ready.")

# number=int(input("Enter a number "))
# if number % 10 ==0:
#         print(f"{number} is a multiple of 10")
# else:
#         print(f"{number} is not multiple of 10")

# prompt= "\nTell me something, and I will repeat it back to you "
# prompt+= "\nEnter 'quit' to end the program. "
# message= ""
# while message != 'quit':
#         message=input(prompt)
#
#         if message!='quit':
#                 print(message)

# prompt= "\nPlease enter the name of a city you have visited "
# prompt+= "\n(Enter 'quit' when you are finished) "
# while True:
#         city = input(prompt)
#         if city == 'quit':
#                 break
#         else:
#                 print(f"I'd love to go to {city.title()} ! ")


# PIZZA TOPPINGS
# prompt= "\nEnter a series of pizza toppings "
# prompt+="\nEnter 'quit' when you are finished "
# while True:
#         pizza=input(prompt)
#         if pizza=='quit':
#                 break
#         else:
#                 print(f"You'll add {pizza} to your pizza")

# MOVIE TICKETS
# prompt = "\nHow old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
#
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#
#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")


# number=int(input("Enter a positive integer: "))
#
# if number<=0:
#         print("\nError: the number must be positive")
# else:
#         for i in range(0,number+1,2):
#                 print(i)



























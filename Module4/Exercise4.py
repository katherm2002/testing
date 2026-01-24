import random

lower=1
upper=10

secret= random.randint (lower, upper)
guess= int(input("Guess a number between 1 and 10: "))

while guess != secret:
    if guess > secret:
        print("Too high!)")
    else:
        print("Too low!)")
    guess = int(input("Guess a number between 1 and 10: "))
print("Correct!")


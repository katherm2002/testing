import random
def dice (a):
    return random.randint(1,a)
dice_number=int(input("Enter number on the dice: "))
result=dice(dice_number)
while result!=dice_number:
    print(result)
    result=dice(dice_number)
print(result)

import random
def dice ():
    return random.randint(1,6)
roll=dice()

while roll != 6:
    print(roll)
    roll=dice()
print(roll)
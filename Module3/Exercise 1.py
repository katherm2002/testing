#Exercise 1, Fisher
length=float(input("enter the length of a zander in cm: "))
if length>=42:
    print("The zander fulfills the size limit")
else:
    length_left= 42 - length
    print(f"Release the fish back into the lake, the fish was {length_left} centimeters below the size limit.")

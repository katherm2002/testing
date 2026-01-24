number = float(input("Enter inches (negative value to stop): "))

while number >= 0:
    centimeters = number * 2.54
    print("Centimeters:", centimeters)
    number = float(input("Enter inches (negative value to stop): "))

print("End")

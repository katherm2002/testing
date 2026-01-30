def gasoline(gal):
    return gal * 3.78541178
volume_gasoline = float(input("Enter the volume in gallons: "))
while volume_gasoline >=0:
    liters = gasoline(volume_gasoline)
    print(liters)
    volume_gasoline = float(input("Enter the volume in gallons: "))
print("You entered a negative number")



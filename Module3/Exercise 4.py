# Exercise 4, years
year = int(input("Enter the year: "))

if year % 4 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("NOT leap Year")
elif year % 400 == 0:
    print("leap Year")

else:
    print("NOT leap Year")
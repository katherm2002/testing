import math
def pizza(diameter, price):
    radio=diameter/2
    area=math.pi * radio**2
    area_in_square_meters=area/10000
    unit_price= price / area_in_square_meters
    return unit_price
diameter_pizza1=float(input("Enter diameter of first pizza: "))
price_pizza1=float(input("Enter price of first pizza: "))
diameter_pizza2=float(input("Enter diameter of second pizza: "))
price_pizza2=float(input("Enter price of second pizza: "))
pizza1=pizza(diameter_pizza1,price_pizza1)
pizza2=pizza(diameter_pizza2,price_pizza2)
if pizza1>pizza2:
    print(f"The second pizza provides better value for money")
else:
    print(f"The first pizza provides better value for money")

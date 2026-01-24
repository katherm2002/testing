# calculate pi
# A= a unit circle, radius of 1
import random
# Ask user how many random (library random) points to generate

number_of_points=int(input("How many random points to generate? "))
points_circle = 0
points_total = 0

while points_total < number_of_points:
    # Generating a point (assigning x and y)
    # N = -1 <= x <= 1 and -1 <=  y <=1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    # check if point is inside the circle
    # n= x^2 + y^2 < 1
    if x ** 2 + y ** 2 < 1:
        points_circle +=1
        points_total +=1

# calculate the approximate value of pi using the method
# pi approx = 4 * n /N
pi_approx=4*points_circle/points_total
print(f"Pi is approximately: {pi_approx}, by generating {points_total} number of points. ")



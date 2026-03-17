import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,number_hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * number_hours

cars = []
for i in range(1,11):
    registration = "ABC-" + str(i)
    max_speed = random.randint(100,200)
    car = Car(registration, max_speed)
    cars.append(car)

race_finished = False
while not race_finished:
    for car in cars:
        change_of_speed = random.randint(-10,15)
        car.accelerate(change_of_speed)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished =True
            break

print(f"{'Registration':<15}{'Max speed':<15}{'Current speed':<18}{'Travelled distance':<20}")
print("-" * 68)

for car in cars:
    print(f"{car.registration_number:<15}{car.max_speed:<15}{car.current_speed:<18}{car.travelled_distance:<20.1f}")
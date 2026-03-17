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

car = Car("ABC-123",142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Registration number: {car.registration_number} "
      f"\nMaximum speed: {car.max_speed}"
      f"\nCurrent speed: {car.current_speed}"
      f"\nTravelled distance: {car.travelled_distance}")
car.accelerate(-200)
print(f"Final speed: {car.current_speed}")
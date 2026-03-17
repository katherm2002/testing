class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123",142)
print(f"Registration number: {car.registration_number} "
      f"\nMaximum speed: {car.max_speed}"
      f"\nCurrent speed: {car.current_speed}"
      f"\nTravelled distance: {car.travelled_distance}")
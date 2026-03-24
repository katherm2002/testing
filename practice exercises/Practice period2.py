class Train:
    def __init__(self,number,max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def travel(self,hours):
        self.travelled_distance += self.current_speed * hours


# Journey exercise
import random
class Journey:
    def __init__(self,name, distance, trains):
        self.name = name
        self.distance = distance
        self.trains = trains

    def hour_passes(self):
        for train in self.trains:
            change = random.randint(-15,20)
            train.accelerate(change)
            train.travel(1)

    def journey_finished(self):
        for train in self.trains:
            if train.travelled_distance >= self.distance:
                return True
        return False

    def print_status(self):
        print(f"{'Train number':>15}{'Max speed':>15}{'Current speed':>18}{'Travelled distance':>20}")
        print("-" * 68)
        for train in self.trains:
            print(f"{train.number:>15}{train.max_speed:>15}{train.current_speed: >18}{train.travelled_distance: > 20.1f}")

# main program
trains=[]
for i in range(1,9):
    number = "TR-" +str(i)
    max_speed= random.randint(120,250)
    train = Train(number,max_speed)
    trains.append(train)
journey = Journey("Northern Express", 6000,trains)

hours = 0
while not journey.journey_finished():
    journey.hour_passes()
    hours += 1

    if hours % 8 == 0:
        journey.print_status()
journey.print_status()




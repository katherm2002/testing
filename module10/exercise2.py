class Elevator:
    def __init__(self, bottom, top_floor):
        self.bottom = bottom
        self.top_floor = top_floor
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
class Building:
    def __init__(self,bottom, top_floor,amount_elevators):
        self.bottom = bottom
        self.top_floor = top_floor
        self.elevators = []

        for i in range(amount_elevators):
            elevator = Elevator(bottom,top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)


building = Building(1,10,3)
building.run_elevator(0,5)
building.run_elevator(1,8)
building.run_elevator(2,3)

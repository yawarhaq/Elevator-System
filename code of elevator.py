class Elevator:
    def __init__(self, elevator_id, num_floors):
        self.elevator_id = elevator_id
        self.num_floors = num_floors
        self.current_floor = 1
        self.direction = 0  # 0: stopped, 1: up, -1: down
        self.requests = []
        self.working = True
        self.door_open = False

    def move(self):
        if self.direction == 1:
            self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1

    def open_door(self):
        self.door_open = True
        print(f"Elevator {self.elevator_id}: Door opened on floor {self.current_floor}")

    def close_door(self):
        self.door_open = False
        print(f"Elevator {self.elevator_id}: Door closed")

    def add_request(self, floor):
        if floor != self.current_floor:
            self.requests.append(floor)
            if self.direction == 0:
                self.direction = 1 if floor > self.current_floor else -1

    def get_next_destination(self):
        if self.requests:
            return self.requests[0]

    def is_moving_up(self):
        return self.direction == 1

    def is_moving_down(self):
        return self.direction == -1


class ElevatorSystem:
    def __init__(self, num_elevators, num_floors):
        self.elevators = [Elevator(i, num_floors) for i in range(1, num_elevators + 1)]

    def request_elevator(self, elevator_id, floor):
        if 1 <= elevator_id <= len(self.elevators):
            self.elevators[elevator_id - 1].add_request(floor)
            print(f"Request added for Elevator {elevator_id} to floor {floor}")
        else:
            print(f"Elevator {elevator_id} does not exist")

    def mark_elevator_maintenance(self, elevator_id):
        if 1 <= elevator_id <= len(self.elevators):
            self.elevators[elevator_id - 1].working = False
            print(f"Elevator {elevator_id} is now in maintenance")
        else:
            print(f"Elevator {elevator_id} does not exist")

    def display_elevator_status(self, elevator_id):
        if 1 <= elevator_id <= len(self.elevators):
            elevator = self.elevators[elevator_id - 1]
            print(f"Elevator {elevator_id} - Current Floor: {elevator.current_floor},"
                  f" Direction: {'Up' if elevator.is_moving_up() else 'Down' if elevator.is_moving_down() else 'Stopped'},"
                  f" Door: {'Open' if elevator.door_open else 'Closed'},"
                  f" Working: {'Yes' if elevator.working else 'No'},"
                  f" Next Destination: {elevator.get_next_destination()}")
        else:
            print(f"Elevator {elevator_id} does not exist")


# Get user inputs for the number of elevators and floors
num_elevators = int(input("Enter the number of elevators: "))
num_floors = int(input("Enter the number of floors: "))
elevator_system = ElevatorSystem(num_elevators, num_floors)

# Example usage loop
while True:
    print("\n--- New Request ---")
    elevator_id = int(input(f"Enter elevator ID (1 to {num_elevators}): "))
    floor = int(input(f"Enter floor for Elevator {elevator_id} request (1 to {num_floors}): "))

    elevator_system.request_elevator(elevator_id, floor)
    elevator_system.display_elevator_status(elevator_id)

    repeat = input("Do you want to make another request? (yes/no): ")
    if repeat.lower() != "yes":
        break











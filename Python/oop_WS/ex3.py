# Approved by: Eitan

from datetime import datetime
import time # For sleep

TIME = 6 # Pause program for N seconds between states

class Machine():
    """ Class of cloud service provider machine """
    def __init__(self, cost):
        self.cost = cost
        self.is_active = False
        self.start_time = 0
        self.active_time = 0
        self.current_cost = 0

    def start_machine(self):
        if not self.is_active:
            self.start_time = datetime.now()
            self.is_active = True
        else:
            print("Machine is already up.")

    def stop_machine(self):
        if self.is_active:
            self.active_time += (datetime.now()- self.start_time).total_seconds()
            self.is_active = False
            self.current_cost += self.cost * self.active_time / 60

    def get_cost(self):
        if self.is_active:
            self.active_time = (datetime.now() - self.start_time).total_seconds()
            return self.current_cost + (self.cost * self.active_time / 60)
        else:
            return self.current_cost


class Type1_Machine(Machine):
    """ Cloud service provider's type 1 machine """
    def __init__(self):
        super().__init__(2)


class Type2_Machine(Machine):
    """ Cloud service provider's type 2 machine """
    def __init__(self):
        super().__init__(5)


class Cloud_Utility():
    """ Class to control machines (create, start, stop)
        Get prices per machine, and total cost
        Cost per minute: Machine 1 --> 2$ |  Machine 2 --> 5$ """
    
    def __init__(self):
        self.machines = []

    def create_machine(self, machine_type):
        if machine_type == 1:
            machine = Type1_Machine()
        elif machine_type == 2:
            machine = Type2_Machine()
        else:
            print("Invalid machine type.")
            return None
        self.machines.append(machine)
        print(f"Machine created successfully, ID is: {len(self.machines)-1}")
        return len(self.machines)-1

    def start_machine(self, id):
        if id < len(self.machines):
            self.machines[id].start_machine()
            print(f"Machine {id} has started.")
        else:
            print("Machine not found.")

    def stop_machine(self, id):
        if id < len(self.machines):
            self.machines[id].stop_machine()
            print(f"Machine {id} has stopped.")
        else:
            print("Machine not found.")

    def cost_per_machine(self, id):
        if id < len(self.machines):
            print(f"Machine {id} cost: {self.machines[id].get_cost()} $")
            return self.machines[id].get_cost()
        else:
            print("Machine not found.")
            return 0

    def total_cost(self):
        total_cost = 0
        for machine in self.machines:
            total_cost += self.cost_per_machine(self.machines.index(machine))
        print(f"Total cost: {total_cost} $")
        return total_cost


if __name__ == "__main__":
    x = Cloud_Utility()

    # ---------- State 1 ----------
    A = x.create_machine(1)
    B = x.create_machine(1)
    C = x.create_machine(1)
    D = x.create_machine(2)

    x.start_machine(A)
    x.start_machine(B)
    x.start_machine(C)
    x.start_machine(D)

    # ---------- State 2 ----------
    time.sleep(TIME)
    E = x.create_machine(2)
    x.start_machine(E)

    # ---------- State 3 ----------
    time.sleep(TIME)
    x.stop_machine(B)

    # ---------- State 4 ----------
    time.sleep(TIME)
    x.cost_per_machine(A)
    x.cost_per_machine(B)
    x.cost_per_machine(C)
    x.cost_per_machine(D)
    x.cost_per_machine(E)
    print("______________________")
    x.total_cost()
class ClusterNode:
    def __init__(self):
        self.speed=0
        self.ignition=False

    def turn_on(self):
        self.ignition=True
        print("Ignition ON")

    def accelerate(self, amount):
        if self.ignition:
            self.speed += amount
            print(f"Speed increases to {self.speed}")

    def brake(self, amount):
        self.speed -= amount
        if self.speed<0:
            self.speed=0
        print(f"Speed decreases to {self.speed}")

car = ClusterNode()

car.turn_on()

car.accelerate(30)

car.brake(10)



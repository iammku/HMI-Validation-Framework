try:
    speed=int("abc")
except ValueError as e:
    print("Invalid input")

try:
    distance=100/0
except ZeroDivisionError:
    print("Cannot be divided by 0")

class Vehicle:
    def __init__(self, speed):
        self.speed=speed
    def validate_speed(self):
        try:
            if self.speed<0:
                raise ValueError
            print("Valid speed")
        except ValueError:
            print("Wrong value")
vehicle1=Vehicle(-120)
vehicle1.validate_speed()

class Vehicle:
    def __init__(self, speed, fuel):
        self.speed=speed
        self.fuel=fuel
    def validate_vehicle(self):
        try:
            if self.speed < 0:
                raise ValueError
            print(f"Valid speed {self.speed}")
            if self.fuel < 0:
                raise ValueError
            print(f"Fuel: {self.fuel}")
        except ValueError:
            print("Invalid Vehicle Data")
v1=Vehicle(120, 50)
v2=Vehicle(-10, 50)
v3=Vehicle(120, -5)
v1.validate_vehicle()
v3.validate_vehicle()
v2.validate_vehicle()
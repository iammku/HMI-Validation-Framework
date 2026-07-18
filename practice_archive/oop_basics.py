#1
class Vehicle:
    pass
vehicle1=Vehicle()
vehicle1.speed=120
print(vehicle1.speed)
print("-"*40)
#2
class Vehicle:
    def start_engine(self):
        print("Ign ON")
vehicle1=Vehicle()
vehicle2=Vehicle()
vehicle1.start_engine()
vehicle2.start_engine()
print("-"*40)
#3
class Vehicle:
    # How Python sees it internally for vehicle1:
    # def __init__(vehicle1):
    def __init__(self):
        print("vehicle object created")
vehicle1=Vehicle()
print("-"*40)
#4
class Vehicle:
    def __init__(self):
        self.warning="Low Fuel"
        self.status="Healthy"
vehicle1=Vehicle()
vehicle2=Vehicle()
print(vehicle1.warning)
print(vehicle1.status)
print(vehicle2.warning)
print("-"*40)
#5
class Vehicle:
    def __init__(self,speed, fuel,door):
        self.speed=speed
        self.fuel=fuel
        self.door=door
vehicle1 = Vehicle(120, 50, "OPEN")
vehicle2 = Vehicle(80, 30, "CLOSED")
print(vehicle1.speed)
print(vehicle1.fuel)
print(vehicle1.door)
print(vehicle2.speed)
print(vehicle2.fuel)
print(vehicle2.door)
print("-"*40)
#6
class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed #The Internal Memory Map: vehicle1.speed = 120
        self.fuel = fuel

    def show_info(self):
        print(self.speed)
        print(self.fuel)
vehicle1=Vehicle(120,80)
#vehicle1.show_info(), Python looks at print(self.speed) and swaps it to:print(vehicle1.speed)
vehicle1.show_info()

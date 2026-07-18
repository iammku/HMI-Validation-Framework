class Vehicle:
    def __init__(self, speed, fuel, door):
        self.speed=speed
        self.fuel=fuel
        self.door=door
    def show_info(self):
        print(f"Fuel: {self.fuel}")
        print(f"Speed:  {self.speed}")
        print(f"Door status: {self.door}")
    def check_health(self):
        has_warnings=False
        if self.speed>=120:
            print("Overspeed")
            has_warnings=True
        if self.fuel<=20:
            print("Low fuel")
            has_warnings=True
        if self.door=="OPEN":
            has_warnings=True
            print("Door ajar")
        if not has_warnings:
            print("Status: HEALTHY (All systems operational)")
        else:
            print("Status: ATTENTION REQUIRED (Active faults on cluster)")
vehicle1 = Vehicle(130, 15, "OPEN")
vehicle1.show_info()
vehicle1.check_health()
print("=" * 45)
vehicle2 = Vehicle(80, 50, "CLOSED")
vehicle2.show_info()
vehicle2.check_health()
class Vehicle:
    def __init__(self, speed, fuel, door):
        self.speed=speed
        self.fuel=fuel
        self.door=door
    def show_info(self):
        print(f"Speed : {self.speed}")
        print(f"Fuel : {self.speed}")
        print(f"Door : {self.speed}")
    def generate_warnings(self):
        warnings=[]
        if self.speed >= 120:
            warnings.append("Overspeed")
        if self.fuel<=20:
            warnings.append("Low fuel")
        if self.door=="OPEN":
            warnings.append("Door ajar")
        return warnings
    def calculate_score(self):
        score=100
        warnings=self.generate_warnings()
        if "Overspeed" in warnings:
            score-=20
        if "Low fuel" in warnings:
            score-=20
        if "Door ajar" in warnings:
            score-=10
        return score
    def get_health_status(self):
        score=self.calculate_score()
        if score>=80:
            return "Healthy"
        elif score>=50:
            return "Warning"
        else:
            return "CRITICAL"
    def display_report(self):
        print("\n===== VEHICLE REPORT =====\n")
        vehicle1.show_info()
        warnings=self.generate_warnings()
        print("\nWarnings:")
        if len(warnings)==0:
            print("No warnings")
        else:
            for warning in warnings:
                print(warning)
        print(f"\nScore is: {self.calculate_score()}")
        print(f"Health status: {self.get_health_status()}")
vehicle1 = Vehicle(130, 15, "OPEN")
vehicle2 = Vehicle(80, 50, "CLOSED")
vehicle1.display_report()
vehicle2.display_report()
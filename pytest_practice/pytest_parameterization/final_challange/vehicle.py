class Vehicle:
    def __init__(self, speed, fuel, battery, door, seatbelt, ignition):
        self.speed=speed
        self.fuel=fuel
        self.battery=battery
        self.door=door
        self.seatbelt=seatbelt
        self.ignition=ignition
    def is_overspeed(self):
        return self.speed>120
    def calculate_health_score(self):
        score=100
        if self.fuel <= 20:
            score-=20
        if self.battery <= 30:
            score-=20
        if self.door == "OPEN":
            score-=10
        if self.seatbelt == "UNBUCKLED":
            score-=10
        if self.ignition == "OFF":
            score-=30
        return score
    def health_status(self):
        score=self.calculate_health_score()
        if score >= 80:
            return "Healthy"
        elif score >= 50:
            return "Warning"
        else:
            return "Critical"
    def generate_warnings(self):
        warnings=[]
        if self.battery <= 30:
            warnings.append("Battery Low")
        if self.fuel <= 20:
            warnings.append("Low Fuel")
        if self.door == "OPEN":
            warnings.append("Door Ajar")
        return warnings
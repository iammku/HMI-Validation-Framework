class Vehicle:
    def __init__(self, speed, fuel, door, seatbelt, ignition, battery):
        self.speed=speed
        self.fuel=fuel
        self.door=door
        self.seatbelt=seatbelt
        self.ignition=ignition
        self.battery=battery
    def calculate_health_score(self):
        score=100
        if self.fuel<=20:
            score-=20
        if self.door=="OPEN":
            score-=10
        if self.seatbelt=="UNBUCKLED":
            score-=10
        if self.battery<=30:
            score-=20
        if self.ignition=="OFF":
            score-=30
        return score
    def health_status(self):
        score=self.calculate_health_score()
        if score>=80:
            return "Healthy"
        if score>=50:
            return "Warning"
        if score<50:
            return "Critical"
    def generate_warnings(self):
        warnings = []
        if self.fuel <= 20:
            warnings.append("Low fuel")
        if self.door == "OPEN":
            warnings.append("Door Ajar")
        if self.battery <=30:
            warnings.append("Battery Low")
        return warnings
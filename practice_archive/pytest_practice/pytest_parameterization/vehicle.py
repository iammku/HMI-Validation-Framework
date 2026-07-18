class Vehicle:
    def __init__(self, speed, fuel, door):
        self.speed=speed
        self.fuel=fuel
        self.door=door
    def health_status(self):
        if self.door=="OPEN":
            return "Critical"
        elif self.fuel<=20:
            return "Warning"
        else:
            return "Healthy"
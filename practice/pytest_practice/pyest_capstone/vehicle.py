class Vehicle:
    def __init__(self, speed, fuel, seatbelt, door, ignition):
        self.speed=speed
        self.fuel=fuel
        self.door=door
        self.seatbelt=seatbelt
        self.ignition=ignition

    def calculate_health(self):
        if self.fuel<=20:
            return "Warning"
        else:
            return "Healthy"
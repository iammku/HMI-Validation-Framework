class Vehicle:
    def __init__(self, speed, fuel, door, ignition, seatbelt):
        self.speed=speed
        self.fuel=fuel
        self.door=door
        self.seatbelt=seatbelt
        self.ignition=ignition
    def get_vehicle_status(self):
        if self.ignition=="ON" and self.door=="CLOSED" and self.seatbelt=="BUCKLED":
            return "Vehicle Ready"
        else:
            return "Vehicle Not Ready"
    def calculate_health(self):
        if self.fuel<=20:
            return "Warning"
        else:
            return "Healthy"
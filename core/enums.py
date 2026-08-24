from enum import Enum

class Gear(Enum):
    PARK = "P"
    REVERSE = "R"
    NEUTRAL = "N"
    DRIVE = "D"

class VehicleEventType(Enum):
    BRAKE = "BRAKE"
    ACCELERATE = "ACCELERATE"
    START_VEHICLE = "START_VEHICLE"
    DOOR_OPEN = "DOOR_OPEN"


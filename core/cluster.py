from core.warning_manager import WarningManager
from core.exception import VehicleStateError
from core.enums import Gear

#VALID_GEARS = ["P", "R", "N", "D"]

class Cluster:

    def __init__(self, abc):
        self._config = abc

        #Managers
        self.warning1 = WarningManager(self)

        #Run time state
        self._speed = abc["speed"]
        #self._gear = abc["gear"]
        self._gear = Gear(abc["gear"])
        self._ignition = abc["ignition"]
        self._seatbelt_fastened = abc.get("seatbelt_fastened")
        self._fuel_level = abc["fuel_level"]

    def show_cluster_info(self):
        print(f"Vehicle: {self.get_vehicle()}")
        print(f"Speed: {self.get_speed()}")
        print(f"Gear: {self.get_gear()}")
        print(f"Theme: {self.get_theme()}")
        print(f"Ignition state: {self.is_ignition_on()}")

    #Getters
    def get_vehicle(self):
        return self._config.get("vehicle")
    def get_speed(self):
        return self._speed
    def get_gear(self):
        return self._gear
    def get_theme(self):
        return self._config["theme"]
    def is_ignition_on(self):
        return self._ignition
    def is_seatbelt_fastened(self):
        return self._seatbelt_fastened
    def get_fuel_level(self):
        return self._fuel_level


    def is_speeding(self):
        return self.get_speed()>100
    def is_dark_theme(self):
        return self.get_theme().lower() == "dark"
    def can_vehicle_move(self):
        return (
            self.is_ignition_on() and
            #self.get_gear().lower() != "park"
            self.get_gear() != Gear.PARK
        )

    #Behaviours
    def start_engine(self):
        self._ignition=True
    def stop_engine(self):
        if self._speed > 0:
            raise VehicleStateError(
                "Cannot stop engine while vehicle moving"
            )
        self._ignition = False

    def shift_gear(self, gear:Gear):
        if not isinstance(gear, Gear):
            raise ValueError(
                f"Invalid gear: {gear}"
            )
        self._gear = gear
    def accelerate(self, increment):
        if not self._ignition:
            raise VehicleStateError(
                "Cannot accelerate because ignition is OFF"
            )
        if self._gear != Gear.DRIVE:
            raise VehicleStateError(
                "Cannot accelerate because gear is not in Drive"
            )
        self._speed+=increment
    def brake(self, decrement):
        self._speed= max(0, self._speed-decrement)
    def fasten_seatbelt(self):
        self._seatbelt_fastened = True
    def unfasten_seatbelt(self):
        self._seatbelt_fastened = False
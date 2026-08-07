from core.warning_manager import WarningManager
class Cluster:
    def __init__(self, abc):
        self._config=abc
        self.warning1=WarningManager(abc)

    def show_cluster_info(self):
        print(f"Vehicle: {self.get_vehicle()}")
        print(f"Speed: {self.get_speed()}")
        print(f"Gear: {self.get_gear()}")
        print(f"Theme: {self.get_theme()}")
        print(f"Ignition state: {self.is_ignition_on()}")
    def get_vehicle(self):
        return self._config.get("vehicle")
    def get_speed(self):
        return self._config["speed"]
    def get_gear(self):
        return self._config["gear"]
    def get_theme(self):
        return self._config["theme"]
    def is_ignition_on(self):
        return self._config["ignition"]
    def is_speeding(self):
        return self.get_speed()>100
    def is_dark_theme(self):
        return self.get_theme().lower() == "dark"
    def can_vehicle_move(self):
        return (
            self.is_ignition_on() and
            self.get_gear().lower() != "park"
        )
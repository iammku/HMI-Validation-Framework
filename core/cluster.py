class Cluster:
    def __init__(self, config):
        self.config=config

    def show_cluster_info(self):
        print(f"Vehicle: {self.get_vehicle()}")
        print(f"Speed: {self.get_speed()}")
        print(f"Gear: {self.get_gear()}")
        print(f"Theme: {self.get_theme()}")
        print(f"Ignition state: {self.is_ignition_on()}")
    def get_vehicle(self):
        return self.config.get("vehicle")
    def get_speed(self):
        return self.config["speed"]
    def get_gear(self):
        return self.config["gear"]
    def get_theme(self):
        return self.config["theme"]
    def is_ignition_on(self):
        return self.config["ignition"]
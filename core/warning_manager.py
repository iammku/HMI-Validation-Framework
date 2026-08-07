class WarningManager:
    """Handles all warnings related logic for cluster"""
    def __init__(self, configx):
        self.config=configx
    def is_seatbelt_warning_active(self):
        return self.config["seatbelt_warning"]
    def is_low_fuel_warning_active(self):
        return self.config.get("low_fuel_warning")


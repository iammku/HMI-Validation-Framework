class WarningManager:
    """Handles all warnings related logic for cluster"""
    def __init__(self, cluster):
        self._cluster=cluster
    def is_seatbelt_warning_active(self):
        """Seatbelt warnings active only when
        vehicle is moving and unbuckled"""
        return (
                self._cluster.get_speed() > 0
                and
                not self._cluster.is_seatbelt_fastened()
        )
    def is_low_fuel_warning_active(self):
        return self._cluster.get_fuel_level() < 15
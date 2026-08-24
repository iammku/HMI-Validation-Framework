from core.enums import Gear, VehicleEventType
from core.vehicle_event import VehicleEvent

class VehicleSimulator:
    """simulate driver actions and external vehicle inputs"""
    def __init__(self, cluster, dispatcher):
        self._cluster = cluster
        self._dispatcher = dispatcher

    # def start_vehicle(self):
    #     return self._cluster.start_engine()
    def start_vehicle(self):
        event = VehicleEvent(
            VehicleEventType.START_VEHICLE
        )
        self._dispatcher.dispatch(event)

    def press_accelerator(self, value):
        event = VehicleEvent(
            VehicleEventType.ACCELERATE,
            value
        )
        self._dispatcher.dispatch(event)

    # def press_brake(self, value):
    #     return self._cluster.brake(value)
    def press_brake(self, value):
        event = VehicleEvent(
            VehicleEventType.BRAKE,
            value
        )
        self._dispatcher.dispatch(event)

    def shift_to_drive(self):
        return self._cluster.shift_gear(Gear.DRIVE)

    def shift_to_park(self):
        self._cluster.shift_gear(Gear.PARK)

    def shift_to_reverse(self):
        self._cluster.shift_gear(Gear.REVERSE)

    def shift_to_neutral(self):
        self._cluster.shift_gear(Gear.NEUTRAL)

    def fasten_seatbelt(self):
        self._cluster.fasten_seatbelt()

    def unfasten_seatbelt(self):
        self._cluster.unfasten_seatbelt()
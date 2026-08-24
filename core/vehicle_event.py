from core.enums import VehicleEventType
from core.exception import EventHandlingError

class VehicleEvent:

    def __init__(self, event_type, *args, **kwargs):
        if not isinstance(event_type, VehicleEventType):
            raise EventHandlingError(
                f"Invalid vehicle event type: {event_type}"
            )
        self.event_type = event_type
        self.args = args
        self.kwargs = kwargs


#event = VehicleEvent(VehicleEventType.BRAKE,10)
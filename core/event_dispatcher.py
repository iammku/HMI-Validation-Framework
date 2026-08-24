from core.enums import VehicleEventType
from core.exception import EventHandlingError

class EventDispatcher:
    # def dispatch(self, event, value):
    #     event(value)
    def __init__(self, cluster):
        self._handlers = {
            VehicleEventType.BRAKE: cluster.brake,
            VehicleEventType.ACCELERATE: cluster.accelerate,
            VehicleEventType.START_VEHICLE: cluster.start_engine,
        }
    def dispatch(self, event):
        if event is None:
            raise EventHandlingError(
                "Vehicle event cannot be None."
            )
        try:
            handler = self._handlers[event.event_type]
        except KeyError as e:
            raise EventHandlingError(
                f"Unsupported vehicle event: {event.event_type}"
            ) from e
            #handler(event.value)
        handler(*event.args,
                **event.kwargs)
#dispatcher = EventDispatcher(cluster)
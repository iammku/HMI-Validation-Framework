"""custom exception used across the framework"""

class ConfigurationError(Exception):
    """Raised when the framework configuration is invalid."""
    pass

class VehicleStateError(Exception):
    """Raised when Invalid vehicle operation"""
    pass

class EventHandlingError(Exception):
    """Raised when a vehicle event cannot be handled."""
    pass
"""Custom Exceptions for the nautobot_plugin_chatops_nso plugin."""


class CommunicationError(Exception):
    """Error communicating with NSO."""


class DeviceNotFound(Exception):
    """Device not found in NSO."""


class DeviceNotSupported(Exception):
    """Device not supported in NSO."""


class DeviceLocked(Exception):
    """Device not reachable in NSO."""

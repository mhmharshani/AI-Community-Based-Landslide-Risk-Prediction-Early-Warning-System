from enum import Enum

class AlertSource(str,Enum):
    SYSTEM = "SYSTEM"
    MANUAL = "MANUAL"
    SENSOR = "SENSOR"
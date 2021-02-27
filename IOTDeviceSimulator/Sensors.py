from datetime import datetime as dt
from enum import Enum


class TemperatureScale(Enum):
    CELSIUS = 1
    FAHRENHEIT = 2


class Sensor:
    def __init__(self, measured_val=None):
        self.timestamp = dt.utcnow()
        self.measured_value = measured_val

    @property
    def timestamp(self, value):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value=dt.utcnow()):
        if not isinstance(value, dt):
            raise Exception("Timestamp value passed is not a datetime object")
        self.__timestamp = value

    @property
    def measured_value(self):
        return self.__measured_value

    @measured_value.setter
    def measured_value(self, value=0):
        self.__measured_value = value


class Temperature(Sensor):
    def __init__(self, measured_value=0.0, temperature_scale=TemperatureScale.CELSIUS):
        Sensor.__init__(self, measured_value)
        self.temperature_scale = temperature_scale

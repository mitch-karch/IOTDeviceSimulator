import datetime.datetime as dt
from enum import Enum


class TemperatureScale(Enum):
    CELSIUS = 1
    FAHRENHEIT = 2


class Sensor:
    def __init__(self):
        self.timestamp = dt.now()
        self.measured_value = None

    @property
    def timestamp(self,value):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value=dt.now()):
        if not isinstance(value, dt.datetime):
            raise Exception("Timestamp value passed is not a datetime object")
        self.__timestamp = value
    
    @property
    def value(self):
        return self.__measured_value

    def value(self, value=0):
        self.__measured_value = value


class Temperature(Sensor):
    def __init__(self, measured_value=0.0, temperature_scale=TemperatureScale.CELSIUS):
        Sensor.__init__(measured_value)
        self.measured_value = measured_value
        self.temperature_scale = temperature_scale

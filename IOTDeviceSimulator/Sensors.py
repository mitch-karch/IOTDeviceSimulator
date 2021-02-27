from datetime import datetime as dt
from enum import Enum


class TemperatureScale(Enum):
    CELSIUS = 1
    FAHRENHEIT = 2


class SensorState(Enum):
    ON = 1
    OFF = 2
    ERROR = 3


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
    def measured_value(self, value=None):
        self.__measured_value = value


class Temperature(Sensor):
    def __init__(self, measured_value=0.0, temperature_scale=TemperatureScale.CELSIUS):
        Sensor.__init__(self, measured_value)
        self.temperature_scale = temperature_scale


class Latch(Sensor):
    def __init__(self, sensor_state=SensorState.OFF):
        Sensor.__init__(self, sensor_state)


class GPS(Sensor):
    def __init__(self, lat=37.874772, longi=-122.258674):
        Sensor.__init__(self)
        self.latitude = lat
        self.longitude = longi

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value=None):
        if not isinstance(value, float):
            raise Exception("Latitude must be a float")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value=None):
        if not isinstance(value, float):
            raise Exception("Longitude must be a float")
        self.__longitude = value

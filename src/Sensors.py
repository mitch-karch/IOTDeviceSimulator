from datetime import datetime as dt
from enum import Enum
import random


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))


class TemperatureScale(ExtendedEnum):
    CELSIUS = 1
    FAHRENHEIT = 2


class SensorState(ExtendedEnum):
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
        self.timestamp = dt.utcnow()
        self.__measured_value = value

    def __str__(self):
        return str(self.measured_value)


class Temperature(Sensor):
    def __init__(self, measured_value=0.0, temperature_scale=TemperatureScale.CELSIUS):
        Sensor.__init__(self, measured_value)
        self.temperature_scale = temperature_scale

    def generate_values(self):
        self.measured_value += random.normalvariate(0, 2.7)


class Latch(Sensor):
    def __init__(self, sensor_state=SensorState.OFF):
        Sensor.__init__(self, sensor_state.name)

    def open(self):
        self.measured_value = SensorState.ON.name

    def close(self):
        self.measured_value = SensorState.OFF.name

    def generate_values(self):
        self.measured_value = random.choices(
            SensorState.list(), cum_weights=(5, 98, 100), k=1
        )[0]


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


if __name__ == "__main__":
    a = Latch()
    print("Made a latch:", a)
    a.open()
    print("Open latch:", a)
    a.close()
    print("Close latch:", a)
    a.generate_values()
    print("Random gen val:", a)

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
    """
    Parent base-class for common sensor types

    Attributes
    ----------
    timestamp : datetime.datetime
        UTC timestamp of when Sensor was last accessed
    measured_value : int
        Stored value of sensor. Usually over-written by child-class

    Methods
    -------
    dict_rep():
        returns a dictionary representation of the sensors attributes
    """

    def __init__(self, measured_val=None):
        """
        Constructs all the necessary attributes for the Sensor object

        Paramaters
        ----------
            timestamp : datetime.datetime
                UTC timestamp of when Sensor was last accessed
            measured_value : int
                Stored value of sensor.
        """
        self.timestamp = dt.utcnow()
        self.measured_value = measured_val

    @property
    def timestamp(self):
        """
        Get the stored timestamp
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        """Sets the protected timestamp value

        Raises
        ------
        Exception
            If the given value is not of type datetime
        """
        if not isinstance(value, dt):
            raise Exception("Timestamp value passed is not a datetime object")
        self._timestamp = value

    @property
    def measured_value(self):
        """
        Get the stored measured value
        """
        return self._measured_value

    @measured_value.setter
    def measured_value(self, value):
        """Sets the protected measured value

        Note that this function also updates the timestamp of the instance.
        This is to keep record of when the last time the value was "read"

        Raises
        ------
        Exception
            If the given value is not of type float
        """
        self.timestamp = dt.utcnow()
        self._measured_value = value

    def dict_rep(self):
        """
        Returns a dictionary representation of the sensors attributes

        Returns
        -------
        dict_rep (dict): Dictionary representation of Sensor Attributes
        """
        return {"measured_value": self.measured_value, "timestamp": self.timestamp}

    def __str__(self):
        return str(self.measured_value)


class Temperature(Sensor):
    """
    Temperature Sensor which emulates a typical thermocouple

    Attributes
    ----------
    measured_value : int
        Stored value of sensor.

    temperature_scale : enum
        enum value representing which temperature scale is being used.

    Methods
    -------
    generate_values():
        sets class attribute of measured_value to a positive of or negative
        increment of the previous values
    """

    def __init__(self, measured_value=0.0, temperature_scale=TemperatureScale.CELSIUS):
        """
        Paramaters
        ----------
            measured_value: float
                starting value point of sensor

            temperature_scale : enum
                enum value representing which temperature scale is being used.
        """

        Sensor.__init__(self, measured_value)
        self.temperature_scale = temperature_scale

    def generate_values(self):
        """
        generate_values():
            sets class attribute of measured_value to a positive of or negative
            increment of the previous values
        """
        self.measured_value += random.normalvariate(0, 2.7)


class Latch(Sensor):
    """
    Latch Sensor which emulates a opening and closing Latch

    Attributes
    ----------
    measured_value : enum
        Latch state represented by enum.name

    Methods
    -------
    generate_values():
        sets class attribute of measured_value to a positive of or negative
        increment of the previous values
    """

    def __init__(self, sensor_state=SensorState.OFF):
        """
        Paramaters
        ----------
            sensor_state: enum
                starting value of latch
        """
        super().__init__(sensor_state.name)

    def open(self):
        """Simulates openning of a lid"""
        self.measured_value = SensorState.ON.name

    def close(self):
        """Simulates closing of a lid"""
        self.measured_value = SensorState.OFF.name

    def generate_values(self):
        """Randomly generates a value which opens or closes the lid"""
        self.measured_value = random.choices(
            SensorState.list(), cum_weights=(5, 98, 100), k=1
        )[0]


class GPS(Sensor):
    """
    GPS Sensor which emulates values from a GPS Antenna

    Attributes
    ----------
    latitude : float
        numeric representation of latitude

    longitude : float
        numeric representation of longitude

    Methods
    -------
    generate_values():
        sets class attribute of longitude and latitude to a positive of or
        negative increment of the previous values
    """

    def __init__(self, lat=37.874772, longi=-122.258674):
        """
        Paramaters
        ----------
            lat : float
                The given value of latitude position
            longi : float
                The given value of longitude position
        """

        super().__init__()
        self.latitude = lat
        self.longitude = longi

    @property
    def latitude(self):
        """
        Get the stored latitude
        """
        return self._latitude

    @latitude.setter
    def latitude(self, value=None):
        """Sets the protected latiude value

        Note that it sets the measure_value in the parentclass to None so that
        the timestamp value gets updated.

        Raises
        ------
        Exception
            If the given value is not of type float
        """
        if not isinstance(value, float):
            raise Exception("Latitude must be a float")
        self._latitude = value
        self.measured_value = None

    @property
    def longitude(self):
        """
        Get the stored longitude
        """
        return self._longitude

    @longitude.setter
    def longitude(self, value=None):
        """Sets the protected longitude value

        Note that it sets the measure_value in the parentclass to None so that
        the timestamp value gets updated.

        Raises
        ------
        Exception
            If the given value is not of type float
        """
        if not isinstance(value, float):
            raise Exception("Longitude must be a float")
        self._longitude = value
        self.measured_value = None

    def dict_rep(self):
        """Returns a dictionary of the sensors stored values"""
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp,
        }

    def generate_values(self):
        """Randomly generates a value which opens or closes the lid"""
        self.latitude += random.normalvariate(0, 0.001)
        self.longitude += random.normalvariate(0, 0.001)

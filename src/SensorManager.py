from datetime import datetime as dt
from .Sensors import GPS, Temperature, Latch


class SensorManager:
    """
    Parent base-class for a collection of sensors

    Attributes
    ----------
    GPS : GPS
        GPS simulator sensor simulator
    ambient_temperature : Temperature
        Ambient Temperature sensor simulator
    internal_temperature : Temperature
        Internal Temperature sensor simulator
    Latch : Latch
        Physical Latch sensor simulator

    Methods
    -------
    generate_values():
        iterates through all instantiated objects and runs their
        generate_values() function

    sensor_readings()
        iterates through all instantiated objects and runs their
        dict_rep() function to generate a dictionary of values to return
    """

    def __init__(self):
        """
        Initializes a mock-IOT Device
        """

        self.GPS = GPS()
        self.ambient_temperature = Temperature(30)
        self.internal_temperature = Temperature(5)
        self.Latch = Latch()

    def generate_values(self):
        """
        Iterates through all managed objects and generates new values
        """
        for name, obj in vars(self).items():
            obj.generate_values()

    @property
    def sensor_readings(self):
        """
        Iterates through all managed objects and stores their values in a dict

        Also sets a top-level value called "timestamp" to record when the dict
        was created
        """
        # self.generate_values()
        temp_dict = {name: obj.dict_rep() for name, obj in vars(self).items()}
        temp_dict["timestamp"] = dt.utcnow()

        return temp_dict

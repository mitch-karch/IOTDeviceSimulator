from datetime import datetime as dt
from .Sensors import GPS, Temperature, Latch


class SensorManager:
    def __init__(self):
        self.GPS = GPS()
        self.ambient_temperature = Temperature(30)
        self.internal_temperature = Temperature(5)
        self.Latch = Latch()

    def generate_values(self):
        print("\n",vars(self))
        for name, obj in vars(self).items():
            obj.generate_values()

    @property
    def sensor_readings(self):
        self.generate_values()
        temp_dict = {
            name: obj.dict_rep()
            for name,obj in vars(self).items()
        }
        temp_dict["timestamp"] = dt.utcnow()

        return temp_dict
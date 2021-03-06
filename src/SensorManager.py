from datetime import datetime as dt
from Sensors import GPS, Temperature, Latch


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
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not isinstance(value, dt):
            raise Exception("Timestamp value passed is not a datetime object")
        self._timestamp = value

    @property
    def sensor_readings(self):
        self.generate_values()
        temp_dict = {
            name: obj.dict_rep()
            for name,obj in vars(self).items()
        }
        temp_dict["timestamp"] = dt.utcnow()

        return temp_dict


if __name__ == "__main__":
    x = SensorManager()
    print(x.sensor_readings)
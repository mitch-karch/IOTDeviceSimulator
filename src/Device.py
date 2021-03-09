from .SensorManager import SensorManager
import uuid
import re
import json


class Device:
    def __init__(self, device_name="default name", device_uuid=None, polling_rate=5):
        self.device_name = device_name
        self.device_uuid = uuid.uuid4() if not device_uuid else device_uuid
        self.polling_rate = polling_rate
        self.sensor_manager = SensorManager()

    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        if bool(re.match("^(\w+\s\w+)$", value)):
            self._device_name = value
        else:
            raise Exception("Name must be two words")

    @property
    def device_uuid(self):
        return self._device_uuid

    @device_uuid.setter
    def device_uuid(self, value):
        if len(str(value)) != 36:
            raise Exception("UUID is expected to be 36 characters")
        else:
            self._device_uuid = value

    @property
    def polling_rate(self):
        return self._polling_rate

    @polling_rate.setter
    def polling_rate(self, value):
        if isinstance(value, int):
            self._polling_rate = value
        else:
            raise Exception("Expecting value to be of type int")

    def generate_values(self):
        self.sensor_manager.generate_values()

    def generate_payload(self):
        temp_dict = self.sensor_manager.sensor_readings
        temp_dict["Device_Name"] = self.device_name
        temp_dict["Device_UUID"] = self.device_uuid
        return temp_dict

    def generate_payload_json(self):
        return json.dumps(self.generate_payload(), default=str)


if __name__ == "__main__":
    x = Device()
    print(x.generate_payload())
    print(x.generate_payload_json())
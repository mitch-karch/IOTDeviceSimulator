from .SensorManager import SensorManager
import uuid
import re
import json
import random
import os
import threading
from pathlib import Path


class Device:
    def __init__(self, device_name=None, device_uuid=None, polling_rate=5):
        self.device_name = device_name
        self.__device_uuid = uuid.uuid4() if not device_uuid else device_uuid
        self.__polling_rate = polling_rate
        self.__sensor_manager = SensorManager()
        self.__threadOn = False

    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        if value is None:
            current_path = Path(os.path.dirname(os.path.realpath(__file__)))
            adjectives = current_path / "resources" / "adjectives.txt"
            nouns = current_path / "resources" / "nouns.txt"

            adjective = random.choice(list(open(adjectives))).rstrip()
            noun = random.choice(list(open(nouns))).rstrip()

            self._device_name = "{} {}".format(adjective, noun)
        elif bool(re.match("^(\w+\s\w+)$", value)):
            self._device_name = value
        else:
            raise Exception("Name must be two words")

    @property
    def device_uuid(self):
        return self.__device_uuid

    @device_uuid.setter
    def device_uuid(self, value):
        if len(str(value)) != 36:
            raise Exception("UUID is expected to be 36 characters")
        else:
            self.__device_uuid = value

    @property
    def polling_rate(self):
        return self.__polling_rate

    @polling_rate.setter
    def polling_rate(self, value):
        if isinstance(value, int):
            self.__polling_rate = value
        else:
            raise Exception("Expecting value to be of type int")

    @property
    def sensor_manager(self):
        return self.__sensor_manager

    def generate_values(self):
        self.sensor_manager.generate_values()

    def generate_payload(self):
        temp_dict = self.sensor_manager.sensor_readings
        temp_dict["Device_Name"] = self.device_name
        temp_dict["Device_UUID"] = self.device_uuid
        return temp_dict

    def generate_payload_json(self):
        return json.dumps(self.generate_payload(), default=str)

    def __str__(self):
        return "Device Name: {}, UUID: {}".format(self.device_name, self.device_uuid)

    def run(self):
        print("Started {} thread".format(self.device_name))
        self.__threadOn = True
        self.do_every(self.polling_rate, self.generate_values)

    def stop(self):
        self.__threadOn = False
        print("Stoped {} thread".format(self.device_name))

    def do_every(self, interval, worker_func):
        if self.__threadOn:
            threading.Timer(interval, self.do_every, [interval, worker_func]).start()

        worker_func()
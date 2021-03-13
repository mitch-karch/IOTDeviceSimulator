from .SensorManager import SensorManager
import uuid
import re
import json
import random
import os
import threading
from datetime import datetime as dt
from pathlib import Path


class Device:
    """
    A device with a sensor manager and other properties

    Attributes
    ----------
    device_name : string
        Short, two-word phrase (adjective, noun) which represents the device
    device_uuid: uuid
        uuid representation associated to a device
    polling_rate: int
        integer representation of how fast each sensor should generate new data
    sensor_manager: SensorManager
        object which manages all sensors
    thread_on: Boolean
        Value which represents if the device's computation thread is started
    start_time: DateTime
        Value which describes the first time that the device was instantiated
        Also known as birthdate
    iterations: int
        Value which represents how many times the device has polled new values

    Methods
    -------
    generate_values():
        iterates through all instantiated objects and runs their
        generate_values() function

    sensor_readings()
        iterates through all instantiated objects and runs their
        dict_rep() function to generate a dictionary of values to return
    """

    def __init__(self, device_name=None, device_uuid=None, polling_rate=5):
        """
        Parameters
        ----------
        device_name : string
            Short, two-word phrase (adjective, noun) which represents the device
        device_uuid: uuid
            uuid representation associated to a device
        polling_rate: int
            integer representation of how fast each sensor should generate new data
        sensor_manager: SensorManager
            object which manages all sensors
        thread_on: Boolean
            Value which represents if the device's computation thread is started
        start_time: DateTime
            Value which describes the first time that the device was instantiated
            Also known as birthdate
        iterations: int
            Value which represents how many times the device has polled new values
        """
        self.device_name = device_name
        self.__device_uuid = uuid.uuid4() if not device_uuid else device_uuid
        self.__polling_rate = polling_rate
        self.__sensor_manager = SensorManager()
        self.__thread_on = False
        self.__start_time = dt.utcnow()
        self.__iterations = 0

    @property
    def device_name(self):
        """
        Get the stored device name
        """
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        """Sets the protected device_name value

        If the value is None, it generates a value from two source files
        to create an "Adjective Noun" two-word phrase

        Raises
        ------
        Exception
            If the given value is not two words seperated by a space
        """
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
        """
        Get the device uuid
        """
        return self.__device_uuid

    @device_uuid.setter
    def device_uuid(self, value):
        if len(str(value)) != 36:
            raise Exception("UUID is expected to be 36 characters")
        else:
            self.__device_uuid = value

    @property
    def polling_rate(self):
        """
        Get the device polling rate
        """
        return self.__polling_rate

    @polling_rate.setter
    def polling_rate(self, value):
        if isinstance(value, int):
            self.__polling_rate = value
        else:
            raise Exception("Expecting value to be of type int")

    @property
    def sensor_manager(self):
        """
        Get the device's sensor manager
        """
        return self.__sensor_manager

    @property
    def iterations(self):
        """
        Get the device's iteration/times that it has generated a value
        """
        return self.__iterations

    @property
    def start_time(self):
        """
        Get the device's birthdate/initialization time
        """
        return self.__start_time

    def generate_values(self):
        """
        Generates new readings for the sensors and also iterates the internal
        counter
        """
        self.sensor_manager.generate_values()
        self.__iterations += 1

    def generate_payload(self):
        """
        Generates and returns a dictionary of values from the sensor readings
        """
        temp_dict = self.sensor_manager.sensor_readings
        temp_dict["Device_Name"] = self.device_name
        temp_dict["Device_UUID"] = self.device_uuid
        return temp_dict

    def generate_payload_json(self):
        """
        Generates and returns a json representation of the JSON values
        """
        return json.dumps(self.generate_payload(), default=str)

    def stats(self):
        """
        Generates and returns the meta-data stats of the instantiated device
        """
        return "Device Name: {}\nBirthdate: {}\nPayloads Geneated:{}\n".format(
            self.device_name, self.start_time, self.iterations
        )

    def __str__(self):
        return "Device Name: {}, UUID: {}".format(self.device_name, self.device_uuid)

    # Threading Things
    def run(self):
        """
        Sets the thread_on value to True so that the generate_values function
        will begin looping at the class's set polling rate
        """
        print("Started {} thread".format(self.device_name))
        self.__thread_on = True
        self.do_every(self.polling_rate, self.generate_values)

    def stop(self):
        """
        Sets the thread_on value to False to stop the thread
        """
        self.__thread_on = False
        print("Stoped {} thread".format(self.device_name))

    def do_every(self, interval, worker_func):
        """
        Function which creates a thread which repeats a given worker_func at a
        given internal

        Reference code from semicolonworld
        """
        if self.__thread_on:
            threading.Timer(interval, self.do_every, [interval, worker_func]).start()

        worker_func()

import unittest
import uuid
from src.Device import Device
from datetime import datetime as dt


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device()
        self.device2 = Device("Jumpy Whale")

    def test_check_initial(self):
        for attrib in ["device_name", "device_uuid", "polling_rate", "sensor_manager"]:
            self.assertTrue(hasattr(self.device, attrib))

    def test_polling_bad_Set(self):
        with self.assertRaises(Exception):
            self.device.polling_rate = "25"

    def test_polling_good_Set(self):
        new_value = 10
        self.device.polling_rate = new_value
        self.assertTrue(self.device.polling_rate == new_value)

    def test_name_bad_Set(self):
        with self.assertRaises(Exception):
            self.device.device_name = "super cool name"

    def test_name_good_Set(self):
        new_name = "sleepy dog"
        self.device.device_name = new_name
        self.assertTrue(self.device.device_name == new_name)

    def test_uuid_bad_Set(self):
        with self.assertRaises(Exception):
            new_uuid = 1234
            self.device.device_uuid = new_uuid

    def test_uuid_good_Set(self):
        new_val = uuid.uuid4()
        self.device.device_uuid = new_val
        self.assertTrue(self.device.device_uuid == new_val)

    def test_payload_contents(self):
        sample_payload = self.device.generate_payload()
        for attrib in [
            "Device_Name",
            "Device_UUID",
            "GPS",
            "ambient_temperature",
            "internal_temperature",
            "Latch",
            "timestamp",
        ]:
            self.assertTrue(attrib in sample_payload)

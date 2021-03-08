import unittest
from src.SensorManager import SensorManager
from datetime import datetime as dt


class TestSensorManager(unittest.TestCase):
    def setUp(self):
        self.SM = SensorManager()

    def test_check_initial(self):
        for attrib in ["GPS", "ambient_temperature", "internal_temperature", "Latch"]:
            self.assertTrue(hasattr(self.SM, attrib))

    def test_valueGen(self):
        old_dict = self.SM.sensor_readings
        new_dict = self.SM.sensor_readings
        self.assertFalse(old_dict == new_dict)

    def test_new_timeStamp(self):
        old_dict = self.SM.sensor_readings
        new_dict = self.SM.sensor_readings
        self.assertFalse(old_dict["timestamp"] == new_dict["timestamp"])


if __name__ == "__main__":
    unittest.main()
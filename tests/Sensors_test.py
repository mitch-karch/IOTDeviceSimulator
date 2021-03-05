import unittest
from src.Sensors import Latch, Temperature, GPS
from datetime import datetime as dt


class TestLatch(unittest.TestCase):
    def setUp(self):
        self.latch = Latch()

    def test_check_initial(self):
        self.assertEqual(self.latch.measured_value, "OFF")

    def test_open_latch(self):
        self.latch.open()
        self.assertEqual(self.latch.measured_value, "ON")

    def test_close_latch(self):
        self.latch.close()
        self.assertEqual(self.latch.measured_value, "OFF")

    def test_timestamp(self):
        self.latch.open()
        difference = dt.utcnow() - self.latch.timestamp
        self.assertTrue(difference.seconds < 5)


class TestTemperature(unittest.TestCase):
    def setUp(self):
        self.temperature = Temperature()

    def test_check_initial(self):
        self.assertTrue(self.temperature.measured_value == 0.0)

    def test_check_change(self):
        self.temperature.generate_values()
        self.assertTrue(-5 <= self.temperature.measured_value <= 5)

    def test_timestamp(self):
        self.temperature.generate_values()
        difference = dt.utcnow() - self.temperature.timestamp
        self.assertTrue(difference.seconds < 5)


class TestGPS(unittest.TestCase):
    def setUp(self):
        self.GPS = GPS()

    def test_check_initial(self):
        self.assertTrue(self.GPS.longitude == -122.258674)
        self.assertTrue(self.GPS.latitude == 37.874772)

    def test_check_bad_set(self):
        with self.assertRaises(Exception):
            self.GPS.latitude = "apple"
        with self.assertRaises(Exception):
            self.GPS.longitude = "apple"

    def test_check_good_Set(self):
        set_long = 34.0099
        set_lat = 118.4960

        self.GPS.longitude = set_long
        self.GPS.latitude = set_lat

        self.assertTrue(self.GPS.longitude == set_long)
        self.assertTrue(self.GPS.latitude == set_lat)

    def test_timestamp(self):
        self.GPS.longitude = 31.0
        difference = dt.utcnow() - self.GPS.timestamp
        self.assertTrue(difference.seconds < 5)



if __name__ == "__main__":
    unittest.main()

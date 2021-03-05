import unittest 
from src.Sensors import Latch


class TestSensorLatch(unittest.TestCase):
    def setUp(self):
        self.latch = Latch()

    def test_check_initial(self):
        self.assertEqual(self.latch.measured_value, "OFF")

    def test_check_change(self):
        self.latch.open()
        self.assertEqual(self.latch.measured_value, "ON")

if __name__ == "__main__":
    unittest.main()
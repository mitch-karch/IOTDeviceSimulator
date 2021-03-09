import unittest
import random
from src.DeviceManager import DeviceManager


class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.DM = DeviceManager()

    def test_check_initial(self):
        self.assertTrue(hasattr(self.DM, "device_list"))

    def test_bad_set(self):
        with self.assertRaises(Exception):
            self.DM.device_list = ["apple"]
            print(self.DM.device_list)

    def test_single_add(self):
        self.DM.add_device()
        self.assertTrue(len(self.DM.device_list) == 1)

    def test_multiple_add(self):
        for _ in range(10):
            self.DM.add_device()
        self.assertTrue(len(self.DM.device_list) == 10)

    def test_single_remove(self):
        self.DM.add_device()
        self.assertTrue(len(self.DM.device_list) == 1)
        temp_uuid = self.DM.device_list[0].device_uuid
        self.DM.remove_device(temp_uuid)
        self.assertTrue(len(self.DM.device_list) == 0)

    def test_multiple_remove(self):
        max_len = 10
        for _ in range(max_len):
            self.DM.add_device()
        self.assertTrue(len(self.DM.device_list) == max_len)

        items_to_remove = random.sample(self.DM.device_list, random.randint(2, max_len))

        for item in items_to_remove:
            self.DM.remove_device(item.device_uuid)

        self.assertTrue(len(self.DM.device_list) == max_len - len(items_to_remove))


if __name__ == "__main__":
    unittest.main()
from .Device import Device


class DeviceManager:
    def __init__(self):
        self.__device_dict = {}

    @property
    def device_dict(self):
        return self.__device_dict

    @device_dict.setter
    def device_dict(self, value):
        if value == {} and len(device_dict) == 0:
            self.__device_dict = value
        else:
            raise Exception("Can't modify the Device dict this way")

    def add_device(self):
        temp_device = Device()
        self.__device_dict[temp_device.device_name] = temp_device
        print("Added {}".format(temp_device))
        del temp_device

    def remove_device(self, name):
        if name in self.__device_dict:
            self.__device_dict[name].stop()
            del self.__device_dict[name]
            print("Removed {}".format(name))
        else:
            print("Device with that Device Name not found")

    def __str__(self):
        return (
            "Device Manager\n"
            + "=" * 10
            + "\n"
            + "\n".join(str(device) for device in self.__device_dict.values())
        )

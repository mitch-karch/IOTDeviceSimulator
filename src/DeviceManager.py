from .Device import Device


class DeviceManager:
    """
    Parent base-class for a collection of Devices

    Attributes
    ----------
    device_dict : dict
        dictionary of devices where hte key is the device's shortname and the
        value is the instantiated device object.

    Methods
    -------
    add_device():
        Generates a new device and adds it to the dictionary

    remove_device(name:str)
        Looks for the device in the device_dict and removes it if it is found,
        prints a warning if it does not find the device.
    """

    def __init__(self):
        """
        Initializes a Device Manager Object
        """
        self.__device_dict = {}

    @property
    def device_dict(self):
        """
        Get the stored device dictionary
        """
        return self.__device_dict

    @device_dict.setter
    def device_dict(self, value):
        """Sets the protected device_name value

        This exists mostly such that the device dictionary cannot be set
        in any way other than the initialization. This probably is unecessary
        since the dict is already private.

        Raises
        ------
        Exception
            If the given value is not an empty dictionary or there are items
            already in the dictionary
        """
        if value == {} and len(device_dict) == 0:
            self.__device_dict = value
        else:
            raise Exception("Can't modify the Device dict this way")

    def add_device(self):
        """
        Generates a new device and adds it to the dictionary
        """

        temp_device = Device()
        self.__device_dict[temp_device.device_name] = temp_device
        print("Added {}".format(temp_device))
        del temp_device

    def remove_device(self, name):
        """
        Looks for the device in the device_dict and removes it if it is found,
        prints a warning if it does not find the device.
        """
        if name in self.__device_dict:
            self.__device_dict[name].stop()
            del self.__device_dict[name]
            print("Removed {}".format(name))
        else:
            print("Device with that Device Name not found")

    def run_device(self, name):
        """
        Looks for the device in the device_dict and run it if it is found,
        prints a warning if it does not find the device.
        """
        if name in self.__device_dict:
            self.__device_dict[name].run()
        else:
            print("Device with that Device Name not found")

    def stop_device(self, name):
        """
        Looks for the device in the device_dict and stop it if it is found,
        prints a warning if it does not find the device.
        """
        if name in self.__device_dict:
            self.__device_dict[name].stop()
        else:
            print("Device with that Device Name not found")

    def find_stats(self, name):
        """
        Looks for the device in the device_dict and display stats it if it is found,
        prints a warning if it does not find the device.
        """
        if name in self.__device_dict:
            print(self.__device_dict[name].stats())
        else:
            print("Device with that Device Name not found")

    def find_payload(self, name):
        """
        Looks for the device in the device_dict and generates a payload if it is found,
        prints a warning if it does not find the device.
        """
        if name in self.__device_dict:
            return self.__device_dict[name].generate_payload()
        else:
            print("Device with that Device Name not found")

    def __str__(self):
        """
        Creates a short representation of all the devices which the dictionary
        is currently holding
        """
        return (
            "Device Manager\n"
            + "=" * 14
            + "\n"
            + "\n".join(str(device) for device in self.__device_dict.values())
        )

from .Device import Device

class DeviceManager:
    def __init__(self):
        self.__device_list = []
    
    @property
    def device_list(self):
        return self.__device_list
    
    @device_list.setter
    def device_list(self,value):
        if value == []:
            self.__device_list = value
        else:
            raise Exception("Can't modify the Device list this way")

    def add_device(self):
        self.__device_list.append(Device())
    
    def remove_device(self,uuid):
        for dev in self.device_list:
            if str(dev.device_uuid) == str(uuid):
                self.__device_list.remove(dev)
    

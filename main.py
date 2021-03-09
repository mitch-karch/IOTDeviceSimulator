from src.DeviceManager import DeviceManager
import threading

DeviceManager = DeviceManager()

# Threading Sample from StackOverflow
class KeyboardThread(threading.Thread):
    def __init__(self, input_cbk=None, name="keyboard-input-thread"):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(input(">"))  # waits to get input + Return


def my_callback(inp):
    # evaluate the keyboard input
    structuredVals = inp.split()

    if structuredVals[0].lower() == "provision":
        DeviceManager.add_device()
    elif structuredVals[0].lower() == "list":
        print(DeviceManager)
    elif structuredVals[0].lower() == "read":
        for device in DeviceManager.device_list:
            if device.device_name == "{} {}".format(
                structuredVals[1], structuredVals[2]
            ):
                print(device.generate_payload())
    elif structuredVals[0].lower() == "run":
        for device in DeviceManager.device_list:
            if device.device_name == "{} {}".format(
                structuredVals[1], structuredVals[2]
            ):
                device.run()
    elif structuredVals[0].lower() == "stop":
        for device in DeviceManager.device_list:
            if device.device_name == "{} {}".format(
                structuredVals[1], structuredVals[2]
            ):
                device.stop()
    elif structuredVals[0].lower() == "stats":
        for device in DeviceManager.device_list:
            if device.device_name == "{} {}".format(
                structuredVals[1], structuredVals[2]
            ):
                print(
                    "Device Name: {}\nBirthdate: {}\nPayloads Geneated:{}\n".format(
                        device.device_name, device.start_time, device.iterations
                    )
                )

# start the Keyboard thread
kthread = KeyboardThread(my_callback)

while True:
    pass
    # the normal program executes without blocking. here just counting up

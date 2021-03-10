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
            self.input_cbk(input("\n>"))  # waits to get input + Return


def my_callback(inp):
    # evaluate the keyboard input
    structuredVals = inp.split()

    if structuredVals[0].lower() == "provision":
        DeviceManager.add_device()
    elif structuredVals[0].lower() == "list":
        print(DeviceManager)
    elif structuredVals[0].lower() == "read":
        given_shortname = "{} {}".format(structuredVals[1], structuredVals[2])
        print(DeviceManager.device_dict[given_shortname].generate_payload())
    elif structuredVals[0].lower() == "run":
        given_shortname = "{} {}".format(structuredVals[1], structuredVals[2])
        DeviceManager.device_dict[given_shortname].run()
    elif structuredVals[0].lower() == "stop":
        given_shortname = "{} {}".format(structuredVals[1], structuredVals[2])
        DeviceManager.device_dict[given_shortname].stop()
    elif structuredVals[0].lower() == "delete":
        DeviceManager.remove_device(
            "{} {}".format(structuredVals[1], structuredVals[2])
        )
    elif structuredVals[0].lower() == "stats":
        given_shortname = "{} {}".format(structuredVals[1], structuredVals[2])
        print(DeviceManager.device_dict[given_shortname].stats())


# start the Keyboard thread
kthread = KeyboardThread(my_callback)

while True:
    pass
    # the normal program executes without blocking. here just counting up

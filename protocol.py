from serial import Serial
from time import sleep

class Protocol():
    def __init__(self, serial_port):
        self.connect_cmd = b"\x11\x51\x04\xB0\x05"
        self.serial_port = Serial(serial_port, 1200, timeout=1)
        # Write something to arduino to wake it up and then wait 2 seconds until its ready
        self.serial_port.write(self.connect_cmd)
        sleep(2)
        


    def get_info(self):
        self.serial_port.write(self.connect_cmd)
        return self.serial_port.read(19)


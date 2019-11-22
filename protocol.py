from serial import Serial
from time import sleep
from serial.tools import list_ports

class Protocol():
    def __init__(self):
        self.connect_cmd = b"\x11\x51\x04\xB0\x05"
        self.basic_read_cmd = b"\x11\x52"
        self.pedal_read_cmd = b"\x11\x53"
        self.throttle_read_cmd = b"\x11\x54"

    
    def connect(self, serial_port):
        self.serial_port = Serial(serial_port, 1200, timeout=1)
        # Wait 2 seconds until Arduino is rebooted after serial connect
        sleep(2) # not necessary if a 10µF C is connected between RESET and GND

    def disconnect(self):
        self.serial_port.close()

    def get_ports(self):
        return list_ports.comports()


    def readinfo(self):
        self.serial_port.write(self.connect_cmd)
        return self.serial_port.read(19)

    def readbasic(self):
        self.serial_port.write(self.basic_read_cmd)
        return self.serial_port.read(27)

    def writebasic(self, baf):
        basic_write_cmd = b'\x16\x52\x24'
        
    
    def readpedal(self):
        self.serial_port.write(self.pedal_read_cmd)
        return self.serial_port.read(14)

    def readthrottle(self):
        self.serial_port.write(self.throttle_read_cmd)
        return True



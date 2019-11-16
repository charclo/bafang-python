from time import sleep
from serial import Serial, SerialException
from serial.tools import list_ports
import sys
#from protocol import connect_cmd, read_cmd, info_message, basic_message, pedal_message, throttle_message



def read_config(cm, answ_format):
    print(cm)
    ser.write(cm)
    ser.flush()
    sleep(1)
    answ = ser.read(100)
    print(answ)
    t = answ_format.parse(answ)
    print(t)

ports_list = list_ports.comports()
if len(ports_list) != 0:
    ser = Serial(ports_list[0].device, 1200, timeout=1)
    ser.write(b"test")
    print(ser)
else:
    print("No Com Ports found")
    sys.exit()

# read_config(connect_cmd.build(
#         dict()), 
#     info_message)

# read_config(read_cmd.build(
#         dict(command = 'BASIC')), 
#     basic_message)

# read_config(read_cmd.build(
#         dict(command = 'PEDAL')), 
#     pedal_message)

# read_config(read_cmd.build(
#         dict(command = 'THROTTLE')), 
#     throttle_message)

ser.close()    

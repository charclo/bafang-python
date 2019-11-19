from collections import namedtuple

class Bafang:
    'class to store all information from bafang controller'

    """     def __init__(self, manufacturer, model, hw_version, fw_version, voltage, max_current, checksum):
        self.manufacturer = manufacturer
        self.model = model
        self.hw_version = hw_version
        self.fw_version = fw_version
        self.voltage = voltage
        self.max_current = max_current
        self.checksum = checksum """

    def __init__(self,):
        self.manufacturer = info_bytes[2:6].decode("utf-8")
        self.model = info_bytes[6:10].decode("utf-8")
        self.hw_version = "V" + '.'.join(str(int(info_bytes[10:12])))
        self.fw_version = "V" + '.'.join(str(int(info_bytes[12:16])))
        self.voltage = 31
        self.max_current = 15
        self.low_battery_protect = 31
        self.limited_current = 15
        self.limited_current_assist0 = 0
        self.limited_current_assist1 = 10
        self.limited_current_assist2 = 20
        self.limited_current_assist3 = 30
        self.limited_current_assist4 = 40
        self.limited_current_assist5 = 50
        self.limited_current_assist6 = 60
        self.limited_current_assist7 = 70
        self.limited_current_assist8 = 80
        self.limited_current_assist9 = 90
        self.limited_speed_assist0 = 1
        self.limited_speed_assist1 = 1
        self.limited_speed_assist2 = 1
        self.limited_speed_assist3 = 1
        self.limited_speed_assist4 = 1
        self.limited_speed_assist5 = 1
        self.limited_speed_assist6 = 1
        self.limited_speed_assist7 = 1
        self.limited_speed_assist8 = 1
        self.limited_speed_assist9 = 1
        self.wheel_diameter = 1
        self.speedmeter_signals = 1
        self.speedmeter_model = 1

    def set_info(self, info_bytes: bytes)

    def store_basic(self, basic_bytes):
        self.low_battery_protect = basic_bytes[2]
        self.limited_current = basic_bytes[3]
        self.limited_current_assist0 = basic_bytes[4]
        self.limited_current_assist1 = basic_bytes[5]
        self.limited_current_assist2 = basic_bytes[6]
        self.limited_current_assist3 = basic_bytes[7]
        self.limited_current_assist4 = basic_bytes[8]
        self.limited_current_assist5 = basic_bytes[9]
        self.limited_current_assist6 = basic_bytes[10]
        self.limited_current_assist7 = basic_bytes[11]
        self.limited_current_assist8 = basic_bytes[12]
        self.limited_current_assist9 = basic_bytes[13]
        self.limited_speed_assist0 = basic_bytes[14]
        self.limited_speed_assist1 = basic_bytes[15]
        self.limited_speed_assist2 = basic_bytes[16]
        self.limited_speed_assist3 = basic_bytes[17]
        self.limited_speed_assist4 = basic_bytes[18]
        self.limited_speed_assist5 = basic_bytes[19]
        self.limited_speed_assist6 = basic_bytes[20]
        self.limited_speed_assist7 = basic_bytes[21]
        self.limited_speed_assist8 = basic_bytes[22]
        self.limited_speed_assist9 = basic_bytes[23]
        self.wheel_diameter = basic_bytes[24]
        self.speedmeter_signals = basic_bytes[25]
        self.speedmeter_model = basic_bytes[25]



    def store_pedal(self, pedal_data):
        print(pedal_data)

    def get_basic(self):
        pass
    
    def get_info(self):
        return [self.manufacturer, self.model, self.hw_version,
                self.fw_version, self.voltage, self.max_current]
                
    def get_info_message(self):
        return self.manufacturer + self.model + self.hw_version + \
                self.fw_version + self.voltage + self.max_current

    def get_pedal(self, basic_data):
        temp = b''
        for b in basic_data:
            temp += b
        return temp

# if __name__ == "__main__":
#     baf = Bafang( b'HZXT', b'SZZ6', b'22', b'2011', b'1', b'20', b'27')
#     fetched_data = (b'HZXT', b'0F', b'22', b'2011', b'1', b'20', b'27', b'HZXT', b'SZZ6', b'22',
#                      b'2011', b'1', b'20', b'HZXT', b'SZZ6', b'22', b'2011', b'1', b'20', b'HZXT', b'SZZ6', b'22', b'2011', b'1', b'20')
#     baf.store_basic(fetched_data)
#     print(baf.limited_current)
#     print(baf.get_pedal(fetched_data))
#     print(baf.get_info_message())

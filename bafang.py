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

    def __init__(self, info_bytes):
        # b'\x02\x10HZXTSZZ6222011\x01\x14\x1b'
        self.manufacturer = info_bytes[2:6].decode("utf-8")
        self.model = info_bytes[6:10].decode("utf-8")
        self.hw_version = int(info_bytes[10:12])
        self.fw_version = int(info_bytes[12:16])
        self.voltage = int(info_bytes[16])
        self.max_current = int(info_bytes[17])
        self.checksum = int(info_bytes[18])

    def store_basic(self, basic_data):
        self.low_battery_protect = basic_data[0]
        self.limited_current = basic_data[1]
        self.limited_current_assist0 = basic_data[2]
        self.limited_current_assist1 = basic_data[3]
        self.limited_current_assist2 = basic_data[4]
        self.limited_current_assist3 = basic_data[5]
        self.limited_current_assist4 = basic_data[6]
        self.limited_current_assist5 = basic_data[7]
        self.limited_current_assist6 = basic_data[8]
        self.limited_current_assist7 = basic_data[9]
        self.limited_current_assist8 = basic_data[10]
        self.limited_current_assist9 = basic_data[11]
        self.limited_speed_assist0 = basic_data[12]
        self.limited_speed_assist1 = basic_data[13]
        self.limited_speed_assist2 = basic_data[14]
        self.limited_speed_assist3 = basic_data[15]
        self.limited_speed_assist4 = basic_data[16]
        self.limited_speed_assist5 = basic_data[17]
        self.limited_speed_assist6 = basic_data[18]
        self.limited_speed_assist7 = basic_data[19]
        self.limited_speed_assist8 = basic_data[20]
        self.limited_speed_assist9 = basic_data[21]
        self.wheel_diameter = basic_data[22]
        self.speedmeter_model = basic_data[23]
        self.speedmeter_signals = basic_data[24]

    def store_pedal(self, pedal_data):
        self.low_battery_protect = pedal_data[0]
        self.limited_current = pedal_data[1]
        self.limited_current_assist0 = pedal_data[2]
        self.limited_current_assist1 = pedal_data[3]
        self.limited_current_assist2 = pedal_data[4]
        self.limited_current_assist3 = pedal_data[5]
        self.limited_current_assist4 = pedal_data[6]
        self.limited_current_assist5 = pedal_data[7]
        self.limited_current_assist6 = pedal_data[8]
        self.limited_current_assist7 = pedal_data[9]
        self.limited_current_assist8 = pedal_data[10]
        self.limited_current_assist9 = pedal_data[11]
        self.limited_speed_assist0 = pedal_data[12]
        self.limited_speed_assist1 = pedal_data[13]
        self.limited_speed_assist2 = pedal_data[14]
        self.limited_speed_assist3 = pedal_data[15]
        self.limited_speed_assist4 = pedal_data[16]
        self.limited_speed_assist5 = pedal_data[17]
        self.limited_speed_assist6 = pedal_data[18]
        self.limited_speed_assist7 = pedal_data[19]
        self.limited_speed_assist8 = pedal_data[20]
        self.limited_speed_assist9 = pedal_data[21]
        self.wheel_diameter = pedal_data[22]
        self.speedmeter_model = pedal_data[23]
        self.speedmeter_signals = pedal_data[24]

    def get_basic(self):
        pass
    
    def get_info(self):
        return [self.manufacturer, self.model, self.hw_version,
                self.fw_version, self.voltage, self.max_current, self.checksum]
                
    def get_info_message(self):
        return self.manufacturer + self.model + self.hw_version + \
                self.fw_version + self.voltage + self.max_current + self.checksum

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

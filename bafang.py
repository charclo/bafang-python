from collections import namedtuple

class Bafang:
    'class to store all information from bafang controller'

    def __init__(self, manufacturer, model, hw_version, fw_version, voltage, max_current, checksum):
        self.manufacturer = manufacturer
        self.model = model
        self.hw_version = hw_version
        self.fw_version = fw_version
        self.voltage = voltage
        self.max_current = max_current
        self.checksum = checksum

    def store_basic(self, basic_data):
        self.low_battery_protect = basic_data['low_battery_protect']
        self.limited_current = basic_data['limited_current']
        self.limited_current_assist0 = basic_data['limited_current_assist0']
        self.limited_current_assist1 = basic_data['limited_current_assist1']
        self.limited_current_assist2 = basic_data['limited_current_assist2']
        self.limited_current_assist3 = basic_data['limited_current_assist3']
        self.limited_current_assist4 = basic_data['limited_current_assist4']
        self.limited_current_assist5 = basic_data['limited_current_assist5']
        self.limited_current_assist6 = basic_data['limited_current_assist6']
        self.limited_current_assist7 = basic_data['limited_current_assist7']
        self.limited_current_assist8 = basic_data['limited_current_assist8']
        self.limited_current_assist9 = basic_data['limited_current_assist9']
        self.limited_speed_assist0 = basic_data['limited_speed_assist0']
        self.limited_speed_assist1 = basic_data['limited_speed_assist1']
        self.limited_speed_assist2 = basic_data['limited_speed_assist2']
        self.limited_speed_assist3 = basic_data['limited_speed_assist3']
        self.limited_speed_assist4 = basic_data['limited_speed_assist4']
        self.limited_speed_assist5 = basic_data['limited_speed_assist5']
        self.limited_speed_assist6 = basic_data['limited_speed_assist6']
        self.limited_speed_assist7 = basic_data['limited_speed_assist7']
        self.limited_speed_assist8 = basic_data['limited_speed_assist8']
        self.limited_speed_assist9 = basic_data['limited_speed_assist9']
        self.wheel_diameter = basic_data['wheel_diameter']
        self.speedmeter_model = basic_data['speedmeter_model']
        self.speedmeter_signals = basic_data['speedmeter_signals']

if __name__ == "__main__":
    baf = Bafang( b'HZXT', b'SZZ6', b'22', b'2011', 1, 20, 27)
    fetched_data = (b'HZXT', b'SZZ6', b'22', b'2011', 1, 20, 27, b'HZXT', b'SZZ6', b'22', b'2011', 1, 20)
    baf.store_basic(fetched_data)
    print(baf.limited_current)

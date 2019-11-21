class Bafang:
    """
    class to store all information from bafang controller
    """

    def __init__(self):
        # info
        self.manufacturer = "N/A"
        self.model = "N/A"
        self.hw_version = "N/A"
        self.fw_version = "N/A"
        self.voltage = "N/A"
        self.max_current = "N/A"
        # TODO : make use of TODOS

        #basic
        self.low_battery_protect = 30
        self.limited_current = 15
        self.limited_current_assist0 = 10
        self.limited_current_assist1 = 20
        self.limited_current_assist2 = 30
        self.limited_current_assist3 = 40
        self.limited_current_assist4 = 50
        self.limited_current_assist5 = 60
        self.limited_current_assist6 = 70
        self.limited_current_assist7 = 80
        self.limited_current_assist8 = 90
        self.limited_current_assist9 = 100
        self.limited_speed_assist0 = 10
        self.limited_speed_assist1 = 20
        self.limited_speed_assist2 = 30
        self.limited_speed_assist3 = 40
        self.limited_speed_assist4 = 50
        self.limited_speed_assist5 = 60
        self.limited_speed_assist6 = 70
        self.limited_speed_assist7 = 80
        self.limited_speed_assist8 = 90
        self.limited_speed_assist9 = 100
        self.wheel_diameter = 1
        self.speedmeter_signals = 1
        self.speedmeter_model = 1

        #pedal

    def set_info(self, info_bytes: bytes):
        """set the info paramaters of bafang"""
        self.manufacturer = info_bytes[2:6].decode("utf-8")
        self.model = info_bytes[6:10].decode("utf-8")
        self.hw_version = "V" + '.'.join(str(int(info_bytes[10:12])))
        self.fw_version = "V" + '.'.join(str(int(info_bytes[12:16])))
        self.voltage = 31
        self.max_current = 15

    def set_basic(self, basic_bytes: bytes):
        """set the basic parameters of bafang"""
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

    def setbasicwithdict(self, basic_dict: dict):
        """set the basic parameters of bafang from a dict """
        for attr, value in basic_dict.items():
            setattr(self, attr, value)

    def set_pedal(self, pedal_data: bytes):
        """set the pedal parameters of bafang"""
        print(pedal_data)

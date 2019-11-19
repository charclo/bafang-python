import json

class JsonWriter():

    def __init__(self, baf):
        self.basic_dict = {
                            'basic_dict': {
                                    "low_battery_protect": baf.low_battery_protect,
                                    "limited_current": baf.limited_current,
                                    "limited_current_assist0": baf.limited_current_assist0,
                                    "limited_current_assist1": baf.limited_current_assist1,
                                    "limited_current_assist2": baf.limited_current_assist2,
                                    "limited_current_assist3": baf.limited_current_assist3,
                                    "limited_current_assist4": baf.limited_current_assist4,
                                    "limited_current_assist5":  baf.limited_current_assist5,
                                    "limited_current_assist6": baf.limited_current_assist6,
                                    "limited_current_assist7": baf.limited_current_assist7,
                                    "limited_current_assist8": baf.limited_current_assist8,
                                    "limited_current_assist9": baf.limited_current_assist9,
                                    "limited_speed_assist0": baf.limited_speed_assist0,
                                    "limited_speed_assist1": baf.limited_speed_assist1,
                                    "limited_speed_assist2": baf.limited_speed_assist2,
                                    "limited_speed_assist3": baf.limited_speed_assist3,
                                    "limited_speed_assist4": baf.limited_speed_assist4,
                                    "limited_speed_assist5": baf.limited_speed_assist5,
                                    "limited_speed_assist6": baf.limited_speed_assist6,
                                    "limited_speed_assist7": baf.limited_speed_assist7,
                                    "limited_speed_assist89": baf.limited_speed_assist9,
                                    "wheel_diameter": baf.wheel_diameter,
                                    "speedmeter_signals": baf.speedmeter_signals,
                                    "speedmeter_model": baf.speedmeter_model
                                }
                            }

    def write_json(self):
        with open('backup.json', 'w') as outfile:
            json.dump(self.basic_dict, outfile, indent=4)
            outfile.close()
            



    def read_json(self):
        with open('backup.json') as json_file:
            data = json.load(json_file)
            for p in basic_dict['basic_dict']:
                print('Name: ' + p['name'])
                print('Website: ' + p['website'])
                print('From: ' + p['from'])
                print('')
                json_file.close()
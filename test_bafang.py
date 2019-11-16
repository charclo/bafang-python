from serial import Serial
from protocol import Protocol
import unittest
from bafang import Bafang


class BafangTest(unittest.TestCase):

    # def test_get_info(self):
    #     protocol = Protocol('/dev/cu.usbmodem142101')
    #     info = protocol.get_info()
    #     self.assertEqual(info, b'\x02\x10HZXTSZZ6222011\x01\x14\x1b')

    def test_bafang_initiation(self):
        baf = Bafang(b'\x02\x10HZXTSZZ6222011\x01\x14\x1b')
        self.assertEqual(baf.manufacturer, 'HZXT')
        self.assertEqual(baf.model, 'SZZ6')
        self.assertEqual(baf.hw_version, 22)
        self.assertEqual(baf.fw_version, 2011)
        self.assertEqual(baf.voltage, 1)
        self.assertEqual(baf.max_current, 20)
        self.assertEqual(baf.checksum, 27)



if __name__ == '__main__':
    unittest.main()
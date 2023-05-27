import sys
import DeviceBase


class SimulatorBRK(DeviceBase.DeviceBase):

    def __init__(self):
        super().__init__(0xfffe, 2)

    def readByte(self, address):
        print("\r\fBRK instruction\r\f")
        sys.exit(0)

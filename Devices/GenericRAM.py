import DeviceBase


class GenericRAM(DeviceBase.DeviceBase):

    def __init__(self, baseAddress, countBytes):

        super().__init__(baseAddress, countBytes)
        self.memory = [0] * countBytes

    def readByte(self, address):

        byte = self.memory[address - self.baseAddress]
        return byte

    def writeByte(self, address, byte):

        self.memory[address - self.baseAddress] = byte

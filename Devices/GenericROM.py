import DeviceBase


class GenericROM(DeviceBase.DeviceBase):

    def __init__(self, baseAddress, countBytes):

        super().__init__(baseAddress, countBytes)
        self.memory = [0] * countBytes

    def readByte(self, address):

        byte = self.memory[address - self.baseAddress]
        return byte

    def writeByte(self, address, byte):

        pass

    def loadFromFile(self, fileName):
        index = 0
        with open(fileName, "rb") as fd:
            while index < self.addressCount and (byte := fd.read(1)):
                self.memory[index] = byte[0]
                index += 1

class DeviceBase:

    def __init__(self, baseAddress, addressCount):

        self.baseAddress = baseAddress
        self.addressCount = addressCount
        self.rangeAddress = baseAddress + addressCount

    def readByte(self, addr):

        pass

    def writeByte(self, addr, value):

        pass

    def isMapped(self, address):

        return address in range(self.baseAddress, self.rangeAddress)

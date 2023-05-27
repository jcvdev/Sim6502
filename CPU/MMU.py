class InvalidAddressException(Exception):

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return "Invalid address: %s" % hex(self.address)


class ValueOutOfRange(Exception):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Value out of range: %s" % hex(self.value)


class MMU:

    def __init__(self):

        self.devices = []

    def addDevice(self, device):

        self.devices.append(device)

    def getDevice(self, address):

        for device in self.devices:
            if device.isMapped(address):
                return device

        raise InvalidAddressException(address)

    def readByte(self, address):

        device = self.getDevice(address)
        return device.readByte(address)

    def writeByte(self, address, byte):

        if byte < 0 or byte > 0xff:
            raise ValueOutOfRange(byte)

        device = self.getDevice(address)
        device.writeByte(address, byte)

    def readWord(self, address):

        return (self.readByte(address + 1) << 8) | self.readByte(address)

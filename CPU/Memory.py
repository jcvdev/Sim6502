'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
from struct import unpack

class Memory(object):
    class InvalidAddressException(BaseException):
        def __init__(self, address):
            self.address = address
            
    class ValueOutOfRange(BaseException):
        def __init__(self, value):
            self.value = value
    
    MEMORYSIZE = 64 * 1024* 1024
    def __init__(self):
        self.memory = bytearray(self.MEMORYSIZE)
        self.protection = bytearray(self.MEMORYSIZE)
        self.maps = {}
        
    def map(self, range, callback):
        self.maps[range] = callback
        
    def unmap(self, range):
        del(self.maps[range])
        
    def readByte(self, address):
        # TODO - add memory mapping
        if address < 0 or address > 0xffff:
            raise self.InvalidAddressException(address)
        
        mapped = [ (range[0], self.maps[range]) for range in self.maps if address>=range[0] and address<=range[1] ]
        if len(mapped):
            base = mapped[0][0]
            mappedDevice = mapped[0][1]
            return mappedDevice.readByte(address - base)
        
        return self.memory[address]
    
    def writeByte(self, address, value):
        # TODO - add memory mapping
        if address < 0 or address > 0xffff:
            raise self.InvalidAddressException(address)
        
        if value < 0 or value > 0xff:
            raise self.ValueOutOfRange(value)

        mapped = [ (range[0], self.maps[range]) for range in self.maps if address>=range[0] and address<range[1] ]
        if len(mapped):
            base = mapped[0][0]
            mappedDevice = mapped[0][1]
            mappedDevice.writeByte(address - base, value)
        else:
            self.memory[address] = value
        
    def readSignedByte(self, address):
        b = self.readByte(address)
        return unpack("b", chr(b))[0]
    
    def readWord(self, address):
        return self.readByte(address) + (self.readByte(address + 1) << 8)
import ROM

class BBCMemoryMap(object):
    def __init__(self, bbc):
        self.bbc = bbc
        
    def readByte(self, address):
        return ROM.rom_os12[address]
    
    def writeByte(self, address, value):
        if address == (0xfe30 - 0xc000):
            self.bbc.setPagedROM(value & 0x0f)
        else:
            pass
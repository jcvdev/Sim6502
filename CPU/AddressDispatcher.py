
class AddressDispatcher(object):
    def __init__(self, registerBank, memory):
        self.registers = registerBank
        self.memory = memory
    
    def implicit(self, data):
        pass
    
    def accumulator(self):
        return self.registers.a
    
    def immediate(self):
        return self.memory.readByte( self.registers.pc + 1)
    
    def zeroPage(self):
        return self.memory.readByte( self.registers.pc + 1)
    
    def zeroPageX(self):
        offset = self.memory.readByte( self.registers.pc + 1)
        addr = (self.registers.x + offset) & 0xff
        return addr
    
    def zeroPageY(self):
        offset = self.memory.readByte( self.registers.pc + 1)
        addr = (self.registers.y + offset) & 0xff
        return addr
    
    def relative(self):
        offset = self.memory.readSignedByte( self.registers.pc + 1)
        return self.registers.pc + 1 + offset
    
    def absolute(self):
        return self.memory.readWord(self.registers.pc + 1)
    
    def absoluteX(self):
        offset = self.memory.readWord(self.registers.pc + 1)
        return self.registers.x + offset
    
    def absoluteY(self):
        offset = self.memory.readWord(self.registers.pc + 1)
        return self.registers.y + offset
        
    def indirect(self):
        addr = self.memory.readWord(self.registers.pc + 1)
        return self.memory.readWord(addr)
    
    def indirectX(self):
        addr = self.memory.readByte(self.registers.pc + 1) + self.registers.x
        addr = addr & 0xff
        return self.memory.readWord(addr)
    
    def indirectY(self):
        addr = self.memory.readByte(self.registers.pc + 1) + self.registers.y
        return self.memory.readWord(addr)
    
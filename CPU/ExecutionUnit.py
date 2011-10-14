'''
Created on 13 Oct 2011

@author: chris.whitworth
'''

class StackOverflowException(BaseException):
    pass
class StackUnderflowException(BaseException):
    pass

class ExecutionDispatcher(object):
    class NotImplementedException(BaseException):
        def __init__(self):
            self.instr = ""
            
        def __repr__(self):
            "%s is not implemented"
            
    def __init__(self, memory, registers):
        self.memory = memory
        self.registers = registers
    
    def pushByte(self, value):
        self.memory.writeByte(self.registers.sp, value)
        self.registers.sp -= 1
        if self.registers.sp < 0x0100:
            raise StackOverflowException()
        
    def pullByte(self):
        self.registers.sp += 1
        if self.registers.sp > 0x01ff:
            raise StackUnderflowException()
        
        return self.memory.readByte(self.registers.sp)
    
    def pushWord(self, value):
        self.pushByte( value >> 8)
        self.pushByte( value & 0xff )

    def pullWord(self):
        lw = self.pullByte()
        hw = self.pullByte() << 8
        return lw + hw
    
    def ADC(self, data, address):
        result = self.registers.a + data + 1 if self.registers.carry else 0
        self.registers.negative = (result & 0x80) != 0 
        self.registers.carry = (result > 255)
        self.registers.zero = (result == 0)
        return result & 0xff

    def AND(self, data, address):
        result = self.registers.a & data
        self.registers.zero = (result == 0)
        self.registers.negative = (result & 0x80) != 0
        return result

    def ASL(self, data, address):
        result = data << 1
        self.registers.carry = (result > 255)
        self.registers.zero = (result == 0)
        self.registers.negative = (result & 0x80) != 0
        return result & 0xff

    def BCC(self, data, address):
        if not self.registers.carry:
            return address
        else:
            return None

    def BCS(self, data, address):
        if self.registers.carry:
            return address
        else:
            return None

    def BEQ(self, data, address):
        if self.registers.zero:
            return address
        else:
            return None

    def BIT(self, data, address):
        result = self.registers.a & data
        self.registers.negative = (result & 0x80) != 0
        self.registers.overflow = (result & 0x40) != 0
        self.registers.zero = (result == 0)
        return None

    def BMI(self, data, address):
        raise self.NotImplementedException()

    def BNE(self, data, address):
        raise self.NotImplementedException()

    def BPL(self, data, address):
        raise self.NotImplementedException()

    def BRK(self, data, address):
        self.pushWord(self.registers.pc + 2)
        self.pushByte(self.registers.ps())
        self.registers.brk = True
        return self.memory.readWord(0xfffe)
        
    def BVC(self, data, address):
        raise self.NotImplementedException()

    def BVS(self, data, address):
        raise self.NotImplementedException()

    def CLC(self, data, address):
        self.registers.carry = False
        return None

    def CLD(self, data, address):
        raise self.NotImplementedException()

    def CLI(self, data, address):
        raise self.NotImplementedException()

    def CLV(self, data, address):
        raise self.NotImplementedException()

    def CMP(self, data, address):
        raise self.NotImplementedException()

    def CPX(self, data, address):
        raise self.NotImplementedException()

    def CPY(self, data, address):
        raise self.NotImplementedException()

    def DEC(self, data, address):
        result = data - 1
        self.registers.zero = (result == 0)
        self.registers.negative = (result & 0x80) != 0
        return result & 0xff

    def DEX(self, data, address):
        result = self.registers.x - 1
        self.registers.zero = (result == 0)
        self.registers.negative = (result & 0x80) != 0
        return result & 0xff

    def DEY(self, data, address):
        result = self.registers.y - 1
        self.registers.zero = (result == 0)
        self.registers.negative = (result & 0x80) != 0
        return result & 0xff

    def EOR(self, data, address):
        result = self.registers.a ^ data
        self.registers.zero = (result == 0)
        self.registers.negative = (result & 0x80) != 0
        return result

    def INC(self, data, address):
        raise self.NotImplementedException()

    def INX(self, data, address):
        raise self.NotImplementedException()

    def INY(self, data, address):
        raise self.NotImplementedException()

    def JMP(self, data, address):
        return address

    def JSR(self, data, address):
        self.pushWord(self.registers.pc + 2)
        return address

    def LDA(self, data, address):
        return data

    def LDX(self, data, address):
        raise self.NotImplementedException()

    def LDY(self, data, address):
        raise self.NotImplementedException()

    def LSR(self, data, address):
        raise self.NotImplementedException()

    def NOP(self, data, address):
        raise self.NotImplementedException()

    def ORA(self, data, address):
        raise self.NotImplementedException()

    def PHA(self, data, address):
        self.pushByte(self.registers.a)
        return None

    def PHP(self, data, address):
        self.pushByte(self.registers.ps())
        return None

    def PLA(self, data, address):
        raise self.NotImplementedException()

    def PLP(self, data, address):
        raise self.NotImplementedException()

    def ROL(self, data, address):
        raise self.NotImplementedException()

    def ROR(self, data, address):
        raise self.NotImplementedException()

    def RTI(self, data, address):
        raise self.NotImplementedException()

    def RTS(self, data, address):
        location = self.pullWord()
        return location + 1

    def SBC(self, data, address):
        raise self.NotImplementedException()

    def SEC(self, data, address):
        raise self.NotImplementedException()

    def SED(self, data, address):
        raise self.NotImplementedException()

    def SEI(self, data, address):
        raise self.NotImplementedException()

    def STA(self, data, address):
        return data

    def STX(self, data, address):
        raise self.NotImplementedException()

    def STY(self, data, address):
        raise self.NotImplementedException()

    def TAX(self, data, address):
        raise self.NotImplementedException()

    def TAY(self, data, address):
        raise self.NotImplementedException()

    def TSX(self, data, address):
        return self.registers.sp

    def TXA(self, data, address):
        return self.registers.x

    def TXS(self, data, address):
        raise self.NotImplementedException()

    def TYA(self, data, address):
        return self.registers.y

    def UNDEFINED(self, data, address):
        raise self.NotImplementedException()

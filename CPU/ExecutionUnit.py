'''
Created on 13 Oct 2011

@author: chris.whitworth
'''

class ExecutionDispatcher(object):
    def __init__(self, memory, registers):
        self.memory = memory
        self.registers = registers
    
    def ADC(self, data):
        pass

    def AND(self, data):
        pass

    def ASL(self, data):
        pass

    def BCC(self, data):
        pass

    def BCS(self, data):
        pass

    def BEQ(self, data):
        pass

    def BIT(self, data):
        pass

    def BMI(self, data):
        pass

    def BNE(self, data):
        pass

    def BPL(self, data):
        pass

    def BRK(self, data):
        pass

    def BVC(self, data):
        pass

    def BVS(self, data):
        pass

    def CLC(self, data):
        pass

    def CLD(self, data):
        pass

    def CLI(self, data):
        pass

    def CLV(self, data):
        pass

    def CMP(self, data):
        pass

    def CPX(self, data):
        pass

    def CPY(self, data):
        pass

    def DEC(self, data):
        pass

    def DEX(self, data):
        pass

    def DEY(self, data):
        pass

    def EOR(self, data):
        pass

    def INC(self, data):
        pass

    def INX(self, data):
        pass

    def INY(self, data):
        pass

    def JMP(self, data):
        pass

    def JSR(self, data):
        pass

    def LDA(self, data):
        pass

    def LDX(self, data):
        pass

    def LDY(self, data):
        pass

    def LSR(self, data):
        pass

    def NOP(self, data):
        pass

    def ORA(self, data):
        pass

    def PHA(self, data):
        pass

    def PHP(self, data):
        pass

    def PLA(self, data):
        pass

    def PLP(self, data):
        pass

    def ROL(self, data):
        pass

    def ROR(self, data):
        pass

    def RTI(self, data):
        pass

    def RTS(self, data):
        pass

    def SBC(self, data):
        pass

    def SEC(self, data):
        pass

    def SED(self, data):
        pass

    def SEI(self, data):
        pass

    def STA(self, data):
        pass

    def STX(self, data):
        pass

    def STY(self, data):
        pass

    def TAX(self, data):
        pass

    def TAY(self, data):
        pass

    def TSX(self, data):
        pass

    def TXA(self, data):
        pass

    def TXS(self, data):
        pass

    def TYA(self, data):
        pass



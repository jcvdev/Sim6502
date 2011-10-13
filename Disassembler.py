'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
import CPU.Dispatch as Dispatch
import CPU.AddressDispatcher as AddressDispatch
import CPU.InstructionDecoder as Decoder
import CPU.Memory as Memory
import CPU.Registers as Registers

import logging

class ExecutionUnit(object):
    def ADC(self, data):
        print "ADC %s" % data

    def AND(self, data):
        print "AND %s" % data

    def ASL(self, data):
        print "ASL %s" % data

    def BCC(self, data):
        print "BCC %s" % data

    def BCS(self, data):
        print "BCS %s" % data

    def BEQ(self, data):
        print "BEQ %s" % data

    def BIT(self, data):
        print "BIT %s" % data

    def BMI(self, data):
        print "BMI %s" % data

    def BNE(self, data):
        print "BNE %s" % data

    def BPL(self, data):
        print "BPL %s" % data

    def BRK(self, data):
        print "BRK %s" % data

    def BVC(self, data):
        print "BVC %s" % data

    def BVS(self, data):
        print "BVS %s" % data

    def CLC(self, data):
        print "CLC %s" % data

    def CLD(self, data):
        print "CLD %s" % data

    def CLI(self, data):
        print "CLI %s" % data

    def CLV(self, data):
        print "CLV %s" % data

    def CMP(self, data):
        print "CMP %s" % data

    def CPX(self, data):
        print "CPX %s" % data

    def CPY(self, data):
        print "CPY %s" % data

    def DEC(self, data):
        print "DEC %s" % data

    def DEX(self, data):
        print "DEX %s" % data

    def DEY(self, data):
        print "DEY %s" % data

    def EOR(self, data):
        print "EOR %s" % data

    def INC(self, data):
        print "INC %s" % data

    def INX(self, data):
        print "INX %s" % data

    def INY(self, data):
        print "INY %s" % data

    def JMP(self, data):
        print "JMP %s" % data

    def JSR(self, data):
        print "JSR %s" % data

    def LDA(self, data):
        print "LDA %s" % data

    def LDX(self, data):
        print "LDX %s" % data

    def LDY(self, data):
        print "LDY %s" % data

    def LSR(self, data):
        print "LSR %s" % data

    def NOP(self, data):
        print "NOP %s" % data

    def ORA(self, data):
        print "ORA %s" % data

    def PHA(self, data):
        print "PHA %s" % data

    def PHP(self, data):
        print "PHP %s" % data

    def PLA(self, data):
        print "PLA %s" % data

    def PLP(self, data):
        print "PLP %s" % data

    def ROL(self, data):
        print "ROL %s" % data

    def ROR(self, data):
        print "ROR %s" % data

    def RTI(self, data):
        print "RTI %s" % data

    def RTS(self, data):
        print "RTS %s" % data

    def SBC(self, data):
        print "SBC %s" % data

    def SEC(self, data):
        print "SEC %s" % data

    def SED(self, data):
        print "SED %s" % data

    def SEI(self, data):
        print "SEI %s" % data

    def STA(self, data):
        print "STA %s" % data

    def STX(self, data):
        print "STX %s" % data

    def STY(self, data):
        print "STY %s" % data

    def TAX(self, data):
        print "TAX %s" % data

    def TAY(self, data):
        print "TAY %s" % data

    def TSX(self, data):
        print "TSX %s" % data

    def TXA(self, data):
        print "TXA %s" % data

    def TXS(self, data):
        print "TXS %s" % data

    def TYA(self, data):
        print "TYA %s" % data

class Disassembler(object):
    def __init__(self, decoderTablePath):
        self.executionDispatcher = ExecutionUnit()
        self.addressDispatcher = AddressDispatch.AddressDispatcher()
        self.decoder = Decoder.Decoder()
        self.memory = Memory.Memory()
        self.registers = Registers.RegisterBank()
        self.dispatch = Dispatch.Dispatcher(self.decoder, self.addressDispatcher, self.executionDispatcher, self.memory, self.registers)

    class Generator(object):
        def __init__(self, dispatcher):
            self.dispatcher = dispatcher
            
        def __iter__(self):
            return self.next()
        
        def next(self):
            while True:
                yield self.dispatch.dispatch()
                
        
    def disassemble(self, data):
        generator = self.Generator(self.decoder, data)
        for decode in generator:
            print decode
        
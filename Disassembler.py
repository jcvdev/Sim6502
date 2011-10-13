'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
import CPU.Dispatch as Dispatch
import CPU.AddressDispatcher as AddressDispatch
import CPU.InstructionDecoder as Decoder
import CPU.Memory as Memory
import CPU.Registers as Registers
import ArrayMemMapper

import logging

class ExecutionUnit(object):
    def ADC(self, data):
        return "ADC %s" % data

    def AND(self, data):
        return "AND %s" % data

    def ASL(self, data):
        return "ASL %s" % data

    def BCC(self, data):
        return "BCC %s" % data

    def BCS(self, data):
        return "BCS %s" % data

    def BEQ(self, data):
        return "BEQ %s" % data

    def BIT(self, data):
        return "BIT %s" % data

    def BMI(self, data):
        return "BMI %s" % data

    def BNE(self, data):
        return "BNE %s" % data

    def BPL(self, data):
        return "BPL %s" % data

    def BRK(self, data):
        return "BRK %s" % data

    def BVC(self, data):
        return "BVC %s" % data

    def BVS(self, data):
        return "BVS %s" % data

    def CLC(self, data):
        return "CLC %s" % data

    def CLD(self, data):
        return "CLD %s" % data

    def CLI(self, data):
        return "CLI %s" % data

    def CLV(self, data):
        return "CLV %s" % data

    def CMP(self, data):
        return "CMP %s" % data

    def CPX(self, data):
        return "CPX %s" % data

    def CPY(self, data):
        return "CPY %s" % data

    def DEC(self, data):
        return "DEC %s" % data

    def DEX(self, data):
        return "DEX %s" % data

    def DEY(self, data):
        return "DEY %s" % data

    def EOR(self, data):
        return "EOR %s" % data

    def INC(self, data):
        return "INC %s" % data

    def INX(self, data):
        return "INX %s" % data

    def INY(self, data):
        return "INY %s" % data

    def JMP(self, data):
        return "JMP %s" % data

    def JSR(self, data):
        return "JSR %s" % data

    def LDA(self, data):
        return "LDA %s" % data

    def LDX(self, data):
        return "LDX %s" % data

    def LDY(self, data):
        return "LDY %s" % data

    def LSR(self, data):
        return "LSR %s" % data

    def NOP(self, data):
        return "NOP %s" % data

    def ORA(self, data):
        return "ORA %s" % data

    def PHA(self, data):
        return "PHA %s" % data

    def PHP(self, data):
        return "PHP %s" % data

    def PLA(self, data):
        return "PLA %s" % data

    def PLP(self, data):
        return "PLP %s" % data

    def ROL(self, data):
        return "ROL %s" % data

    def ROR(self, data):
        return "ROR %s" % data

    def RTI(self, data):
        return "RTI %s" % data

    def RTS(self, data):
        return "RTS %s" % data

    def SBC(self, data):
        return "SBC %s" % data

    def SEC(self, data):
        return "SEC %s" % data

    def SED(self, data):
        return "SED %s" % data

    def SEI(self, data):
        return "SEI %s" % data

    def STA(self, data):
        return "STA %s" % data

    def STX(self, data):
        return "STX %s" % data

    def STY(self, data):
        return "STY %s" % data

    def TAX(self, data):
        return "TAX %s" % data

    def TAY(self, data):
        return "TAY %s" % data

    def TSX(self, data):
        return "TSX %s" % data

    def TXA(self, data):
        return "TXA %s" % data

    def TXS(self, data):
        return "TXS %s" % data

    def TYA(self, data):
        return "TYA %s" % data

class Disassembler(object):
    def __init__(self, decoderTablePath):
        self.executionDispatcher = ExecutionUnit()
        self.memory = Memory.Memory()
        self.registers = Registers.RegisterBank()
        self.addressDispatcher = AddressDispatch.AddressDispatcher(self.memory, self.registers)
        self.decoder = Decoder.Decoder(decoderTablePath)
        self.dispatch = Dispatch.Dispatcher(self.decoder, self.addressDispatcher, self.executionDispatcher, self.memory, self.registers)

    class Generator(object):
        def __init__(self, dispatcher):
            self.dispatcher = dispatcher
            
        def __iter__(self):
            return self.next()
        
        def next(self):
            while True:
                yield self.dispatcher.dispatch()
        
    def disassemble(self, data):
        self.memory.map( (0, len(data)), ArrayMemMapper.Mapper(data))
        generator = self.Generator(self.dispatch)
        for decode in generator:
            print decode
        
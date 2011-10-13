'''
Created on 12 Oct 2011

@author: chris.whitworth
'''

class Dispatcher:
    def __init__(self, decoder, addressDispatcher, executionDispatcher, memory, registers):
        self.decoder = decoder
        self.memory = memory
        self.registers = registers
        self.addressingTable = { "imp": addressDispatcher.implicit,
                                 "acc": addressDispatcher.accumulator,
                                 "imm": addressDispatcher.immediate,
                                 "zp" : addressDispatcher.zeroPage,
                                 "zpx": addressDispatcher.zeroPageX,
                                 "zpy": addressDispatcher.zeroPageY,
                                 "rel": addressDispatcher.relative,
                                 "abs": addressDispatcher.absolute,
                                 "abx": addressDispatcher.absoluteX,
                                 "aby": addressDispatcher.absoluteY,
                                 "ind": addressDispatcher.indirect,
                                 "inx": addressDispatcher.indirectX,
                                 "iny": addressDispatcher.indirectY
                               }
        
        self.executionTable = { "ADC" : executionDispatcher.ADC,
                                "AND" : executionDispatcher.AND,
                                "ASL" : executionDispatcher.ASL,
                                "BCC" : executionDispatcher.BCC,
                                "BCS" : executionDispatcher.BCS,
                                "BEQ" : executionDispatcher.BEQ,
                                "BIT" : executionDispatcher.BIT,
                                "BMI" : executionDispatcher.BMI,
                                "BNE" : executionDispatcher.BNE,
                                "BPL" : executionDispatcher.BPL,
                                "BRK" : executionDispatcher.BRK,
                                "BVC" : executionDispatcher.BVC,
                                "BVS" : executionDispatcher.BVS,
                                "CLC" : executionDispatcher.CLC,
                                "CLD" : executionDispatcher.CLD,
                                "CLI" : executionDispatcher.CLI,
                                "CLV" : executionDispatcher.CLV,
                                "CMP" : executionDispatcher.CMP,
                                "CPX" : executionDispatcher.CPX,
                                "CPY" : executionDispatcher.CPY,
                                "DEC" : executionDispatcher.DEC,
                                "DEX" : executionDispatcher.DEX,
                                "DEY" : executionDispatcher.DEY,
                                "EOR" : executionDispatcher.EOR,
                                "INC" : executionDispatcher.INC,
                                "INX" : executionDispatcher.INX,
                                "INY" : executionDispatcher.INY,
                                "JMP" : executionDispatcher.JMP,
                                "JSR" : executionDispatcher.JSR,
                                "LDA" : executionDispatcher.LDA,
                                "LDX" : executionDispatcher.LDX,
                                "LDY" : executionDispatcher.LDY,
                                "LSR" : executionDispatcher.LSR,
                                "NOP" : executionDispatcher.NOP,
                                "ORA" : executionDispatcher.ORA,
                                "PHA" : executionDispatcher.PHA,
                                "PHP" : executionDispatcher.PHP,
                                "PLA" : executionDispatcher.PLA,
                                "PLP" : executionDispatcher.PLP,
                                "ROL" : executionDispatcher.ROL,
                                "ROR" : executionDispatcher.ROR,
                                "RTI" : executionDispatcher.RTI,
                                "RTS" : executionDispatcher.RTS,
                                "SBC" : executionDispatcher.SBC,
                                "SEC" : executionDispatcher.SEC,
                                "SED" : executionDispatcher.SED,
                                "SEI" : executionDispatcher.SEI,
                                "STA" : executionDispatcher.STA,
                                "STX" : executionDispatcher.STX,
                                "STY" : executionDispatcher.STY,
                                "TAX" : executionDispatcher.TAX,
                                "TAY" : executionDispatcher.TAY,
                                "TSX" : executionDispatcher.TSX,
                                "TXA" : executionDispatcher.TXA,
                                "TXS" : executionDispatcher.TXS,
                                "TYA" : executionDispatcher.TYA
                                }
    
    def addressDecode(self, opcode):
        addressingMode = self.decoder.addressingMode(opcode)
        return self.addressingTable[addressingMode]()
    
    def dispatch(self):
        opcode = self.memory.readByte(self.registers.pc)
        instruction = self.decoder.instruction(opcode)
        data = self.addressDecode(opcode)
        self.executionTable[instruction](data)
        self.registers.pc += self.decoder.instructionLength(opcode)
        
        
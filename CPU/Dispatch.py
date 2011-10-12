'''
Created on 12 Oct 2011

@author: chris.whitworth
'''

class Dispatcher:
    def __init__(self, decoder, addressDispatcher, executionDispatcher):
        self.decoder = decoder
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
    
    def addressDecode(self, opcode, data):
        addressingMode = self.decoder.addressingMode(opcode)
        data = self.addressingTable[addressingMode]()
    
    def dispatch(self, opcode, data):
        pass
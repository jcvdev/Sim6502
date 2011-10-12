'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
import CPU.InstructionDecoder as InstructionDecoder
import logging

class Disassembler(object):
    def __init__(self, decoderTablePath):
        self.decoder = InstructionDecoder.Decoder(decoderTablePath)

    class Generator(object):
        def __init__(self, decoder, data):
            self.decoder = decoder
            self.data = data
            self.index = 0
            
        def __iter__(self):
            return self.next()
        
        def next(self):
            while(self.index < len(self.data)):
                opcode = self.data[self.index]
                logging.info("Decoding %s" % hex(opcode))
                instructionLength = self.decoder.instructionLength(opcode)
                decode = "%s " % self.decoder.instruction(opcode)
               
                decode += " ".join( [ hex(self.data[self.index + 1 + b]) for b in range(instructionLength -1 )]) 
                
                self.index += instructionLength
                
                yield decode
        
    def disassemble(self, data):
        generator = self.Generator(self.decoder, data)
        for decode in generator:
            print decode
        
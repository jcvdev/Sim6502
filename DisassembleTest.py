'''
Created on 12 Oct 2011

@author: chris.whitworth
'''

import Disassembler
import ROMs.BBCMicro as BBC

DecoderTablePath = "insts.csv"

def main():
    disassembler = Disassembler.Disassembler(DecoderTablePath)
    disassembler.disassemble(BBC.rom_os12)
    
    
if __name__ == '__main__':
    main()
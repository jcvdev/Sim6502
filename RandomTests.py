'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
import unittest
import CPU.Memory as Memory
import CPU.Registers as Registers
import CPU.AddressDispatcher as AddressDispatcher
import CPU.Writeback as Writeback
import CPU.ExecutionUnit as ExecutionUnit
import CPU.Dispatch as Dispatch
import CPU.InstructionDecoder as Decoder
import ROMs.BBCMicro as Beeb
import ROMs.TestData as TestData
import ArrayMemMapper
import Debugging.Combiner
import Debugging.Writeback
import Debugging.ExecutionUnit

DecodeFilename = "insts.csv"


class Test(unittest.TestCase):

    def testName(self):
        testRom = Beeb.rom_os12
        basicRom = Beeb.rom_basic2
        
        mem = Memory.Memory()
        reg = Registers.RegisterBank()
        addrDispatch = AddressDispatcher.AddressDispatcher(mem,reg)
        
        
        execDispatch = ExecutionUnit.ExecutionDispatcher(mem,reg)
        execLogger = Debugging.ExecutionUnit.LoggingExecutionUnit()
        combinedExec = Debugging.Combiner.Dispatcher( (execLogger, execDispatch) )
        
        writebackDispatch = Writeback.Dispatcher(mem,reg)
        writebackLogger = Debugging.Writeback.LoggingDispatcher()
        combinedWriteback = Debugging.Combiner.Dispatcher( (writebackLogger, writebackDispatch) )
        
        decoder = Decoder.Decoder(DecodeFilename)
        
        dispatch = Dispatch.Dispatcher(decoder, addrDispatch, combinedExec, combinedWriteback, mem, reg)
        
        mem.map( (0xc000, 0xc000 + len(testRom)), ArrayMemMapper.Mapper(testRom))
        mem.map( (0x8000, 0x8000 + len(basicRom)), ArrayMemMapper.Mapper(basicRom))
        
        mem.writeByte(0xfffc, 0x00)
        mem.writeByte(0xfffd, 0xff)
        mem.writeByte(0xfffe, 0x0b)
        mem.writeByte(0xffff, 0xff)
        
        reg.pc = mem.readWord(0xfffc)
        
        while True:
            dispatch.dispatch()
            reg.status()
#            raw_input("<enter>")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

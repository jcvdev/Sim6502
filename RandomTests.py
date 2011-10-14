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
        
        mem.map( (0xff00, 0xff00 + len(TestData.testROM1)), ArrayMemMapper.Mapper(TestData.testROM1))
        reg.pc = 0xff00
        
        while True:
            dispatch.dispatch()
            reg.status()
            raw_input("<enter>")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

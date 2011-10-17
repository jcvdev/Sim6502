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
import Debugging.Combiner
import Debugging.Writeback
import Debugging.ExecutionUnit
import BBCMicro.System

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
        
        pcTrace = False
        verbose = False
        
        dispatch = None
        if verbose:
            dispatch = Dispatch.Dispatcher(decoder, addrDispatch, combinedExec, combinedWriteback, mem, reg)
        else:
            dispatch = Dispatch.Dispatcher(decoder, addrDispatch, execDispatch, writebackDispatch, mem, reg)
        
        bbc = BBCMicro.System.Beeb(dispatch)
              
        OS_WRCH = 0xe0a4
        OS_RDCH = 0xdec5
        instr = 0
        
        while True:
            if reg.pc == 0x8000:
                verbose = True
            
            if pcTrace:
                print "%s: PC: %s" % (instr, hex(reg.pc))
            instr += 1

            if not pcTrace and not verbose:
                if reg.pc == OS_WRCH:
                    print chr(reg.a),
                elif reg.pc == OS_RDCH:
                    print "OS_RDCH"
            
            bbc.tick() 
           
            if verbose:
                reg.status()
            
            #raw_input("<enter>")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

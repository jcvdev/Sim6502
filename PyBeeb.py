'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
import sys
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

class BBC(object):
    def __init__(self, pcTrace = False, verbose = False):
        self.mem = Memory.Memory()
        self.reg = Registers.RegisterBank()
        addrDispatch = AddressDispatcher.AddressDispatcher(self.mem, self.reg)

        execDispatch = ExecutionUnit.ExecutionDispatcher(self.mem,self.reg)
        execLogger = Debugging.ExecutionUnit.LoggingExecutionUnit()
        combinedExec = Debugging.Combiner.Dispatcher( (execLogger, execDispatch) )

        writebackDispatch = Writeback.Dispatcher(self.mem,self.reg)
        writebackLogger = Debugging.Writeback.LoggingDispatcher()
        combinedWriteback = Debugging.Combiner.Dispatcher( (writebackLogger, writebackDispatch) )

        decoder = Decoder.Decoder(DecodeFilename)

        self.pcTrace = pcTrace
        self.verbose = verbose

        dispatch = None
        if verbose:
            dispatch = Dispatch.Dispatcher(decoder, addrDispatch,
                                           combinedExec, combinedWriteback,
                                           self.mem, self.reg)
        else:
            dispatch = Dispatch.Dispatcher(decoder, addrDispatch,
                                           execDispatch, writebackDispatch,
                                           self.mem, self.reg)

        self.bbc = BBCMicro.System.Beeb(dispatch)

    def go(self, syscalls):
        instr = 0

        while True:
            if self.pcTrace:
                print "%s: PC: %s" % (instr, hex(self.reg.pc))
            instr += 1

            if not self.pcTrace and not self.verbose:
                if self.reg.pc in syscalls.keys():
                    syscalls[self.reg.pc](self.reg, self.mem)

            self.bbc.tick()

            if self.verbose:
                self.reg.status()

def OS_WRCH(reg,mem): sys.stdout.write(chr(reg.a))
def OS_RDCH(reg,mem): print "OS_RDCH" # Could inject keypresses here maybe?

if __name__ == "__main__":
    OS_WRCH_LOC = 0xe0a4
    OS_RDCH_LOC = 0xdec5
    syscalls = { OS_WRCH_LOC : OS_WRCH,
                 OS_RDCH_LOC : OS_RDCH }
    bbc = BBC()
    bbc.go(syscalls)

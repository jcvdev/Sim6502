'''
Created on 12 Oct 2011

@author: chris.whitworth
'''
import unittest
import CPU.Memory as Memory
import CPU.Registers as Registers
import CPU.AddressDispatcher as AddressDispatcher
import CPU.Dispatch as Dispatch
import CPU.InstructionDecoder as Decoder

DecodeFilename = "insts.csv"


class Test(unittest.TestCase):

    def testName(self):
        mem = Memory.Memory()
        mem.map()
        reg = Registers.RegisterBank()
        addrDispatch = AddressDispatcher.AddressDispatcher(reg, mem)
        decoder = Decoder.Decoder(DecodeFilename)
        dispatch = Dispatch.Dispatcher(decoder, addrDispatch, None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

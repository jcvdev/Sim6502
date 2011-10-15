'''
Created on 12 Oct 2011

@author: chris.whitworth
'''

class RegisterBank(object):
    def __init__(self):
        self.pc = 0x0000
        self.sp = 0x01ff
        self.a  = 0x00
        self.x  = 0x00
        self.y  = 0x00
        self.nextPC = 0x0000
        
        self.carry = False
        self.zero = False
        self.int = False
        self.dec = False
        self.brk = False
        self.overflow = False
        self.negative = False
        
    def ps(self):
        return ( (1 if self.carry else 0) |
                 (2 if self.zero else 0) |
                 (4 if self.int else 0) |
                 (8 if self.dec else 0) |
                 (16 if self.brk else 0) |
                 (32 if self.overflow else 0) |
                 (64 if self.negative else 0) )
        
    def setPS(self, value):
        self.carry = (value & 0x1) != 0
        self.zero = (value & 0x2) != 0
        self.int = (value & 0x4) != 0
        self.dec = (value & 0x8) != 0
        self.brk = (value & 0x10) != 0
        self.overflow = (value & 0x20) != 0
        self.negative = (value & 0x40) != 0
        
    def status(self):
        print "A = %s X = %s Y = %s" % (hex(self.a), hex(self.x), hex(self.y))
        print "PC = %s SP = %s" % (hex(self.pc), hex(self.sp))
        print "C = %s Z = %s I = %s D = %s" % (self.carry, self.zero, self.int, self.dec)
        print "B = %s V = %s N = %s" % (self.brk, self.overflow, self.negative)
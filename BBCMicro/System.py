'''
Created on 16 Oct 2011

@author: Chris
'''
import OS
import PagedROM
import Sheila

class Beeb(object):
    def __init__(self, cpu):
        self.os = OS.BBCMemoryMap(self)
        self.pagedROM = PagedROM.PagedROM()
        self.sheila = Sheila.Sheila()
        
        cpu.memory.map( (0xc000, 0xffff), self.os)
        cpu.memory.map( (0x8000, 0xbfff), self.pagedROM)
        cpu.memory.map( (0xfe00, 0xfeff), self.sheila)

        self.cpu = cpu
        self.cpu.reset()
        self.setPagedROM(0)
#        self.cpu.memory.writeByte(0x028c, 15)
        
    def setPagedROM(self, pagedRom):
        self.pagedROM.setPagedROM(pagedRom)
    
    def tick(self):
        self.cpu.dispatch()
class AddressDispatcher:

    def __init__(self, mmu, registerBank):
        self.registers = registerBank
        self.mmu = mmu
        self.disassembleString = None

    def implicit(self):
        self.disassembleString = None
        return None

    def accumulator(self):
        self.disassembleString = None
        return None

    def immediate(self):
        addr = self.registers.pc + 1
        self.disassembleString = "#$%02x" % (self.mmu.readByte(addr))
        return addr

    def zeroPage(self):
        addr = self.mmu.readByte(self.registers.pc + 1)
        self.disassembleString = "$%02x" % (addr)
        return addr

    def zeroPageX(self):
        base = self.mmu.readByte(self.registers.pc + 1)
        addr = base + self.registers.x
        self.disassembleString = "($%02x,x)" % (base)
        return addr & 0xffff

    def zeroPageY(self):
        base = self.mmu.readByte(self.registers.pc + 1)
        addr = base + self.registers.y
        self.disassembleString = "($%02x),y" % (base)
        return addr & 0xffff

    def relative(self):
        byte = self.mmu.readByte(self.registers.pc + 1)
        offset = byte if byte < 128 else byte - 256
        addr = offset + self.registers.nextPC
        self.disassembleString = "$%04x" % (addr)
        return addr

    def absolute(self):
        addr = self.mmu.readWord(self.registers.pc + 1)
        self.disassembleString = "$%04x" % (addr)
        return addr

    def absoluteX(self):
        base = self.mmu.readWord(self.registers.pc + 1)
        addr = base + self.registers.x
        self.disassembleString = "$%04x,x" % (addr)
        return addr & 0xffff

    def absoluteY(self):
        base = self.mmu.readWord(self.registers.pc + 1)
        addr = base + self.registers.y
        self.disassembleString = "$%04x,y" % (addr)
        return addr & 0xffff

    def indirect(self):
        addr = self.mmu.readWord(self.mmu.readWord(self.registers.pc + 1))
        self.disassembleString = "($%04x)" % (addr)
        return addr & 0xffff

    def indirectX(self):
        base = self.mmu.readByte(self.registers.pc + 1)
        addr = self.mmu.readWord((base + self.registers.x) & 0xff)
        self.disassembleString = "($%04x,x)" % (base)
        return addr & 0xffff

    def indirectY(self):
        base = self.mmu.readByte(self.registers.pc + 1)
        addr = self.mmu.readWord(base) + self.registers.y
        self.disassembleString = "($%02x),y" % (base)
        return addr

    def implicitRead(self):
        return None

    def accumulatorRead(self):
        return self.registers.a

    def immediateRead(self):
        return self.mmu.readByte(self.immediate())

    def zeroPageRead(self):
        return self.mmu.readByte(self.zeroPage())

    def zeroPageXRead(self):
        return self.mmu.readByte(self.zeroPageX())

    def zeroPageYRead(self):
        return self.mmu.readByte(self.zeroPageY())

    def relativeRead(self):
        return self.mmu.readByte(self.relative())  # hack hack hack

    def absoluteRead(self):
        return self.mmu.readByte(self.absolute())

    def absoluteXRead(self):
        return self.mmu.readByte(self.absoluteX())

    def absoluteYRead(self):
        return self.mmu.readByte(self.absoluteY())

    def indirectRead(self):
        return self.mmu.readByte(self.indirect())

    def indirectXRead(self):
        return self.mmu.readByte(self.indirectX())

    def indirectYRead(self):
        return self.mmu.readByte(self.indirectY())

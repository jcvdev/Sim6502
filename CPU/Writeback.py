class Dispatcher:

    def __init__(self, mmu, registers):
        self.mmu = mmu
        self.registers = registers

    def A(self, value, location):
        self.registers.a = value

    def X(self, value, location):
        self.registers.x = value

    def Y(self, value, location):
        self.registers.y = value

    def mem(self, value, location):
        self.mmu.writeByte(location, value)

    def PC(self, value, location):
        self.registers.nextPC = value

    def SP(self, value, location):
        self.registers.sp = value

    def PS(self, value, location):
        self.registers.setPS(value)

    def NW(self, value, location):
        pass

import CPU.MMU as MMU
import CPU.Registers as Registers
import CPU.AddressDispatcher as AddressDispatcher
import CPU.Writeback as Writeback
import CPU.ExecutionUnit as ExecutionUnit
import CPU.Dispatch as Dispatch
import CPU.InstructionDecoder as Decoder

import Devices.GenericRAM as GenericRAM
import Devices.GenericROM as GenericROM

if __name__ == "__main__":

    RAM = GenericRAM.GenericRAM(0x0000, 0x8000)
    ROM = GenericROM.GenericROM(0xc000, 0x4000)
    BRK = SimulatorBRK.SimulatorBRK()
    ROM.loadFromFile("firmware.bin")

    mmu = MMU.MMU()
    mmu.addDevice(BRK)  # Must be added first to handle 0xfffe address before any other device
    mmu.addDevice(RAM)
    mmu.addDevice(ROM)

    registers = Registers.RegisterBank()
    addrDispatch = AddressDispatcher.AddressDispatcher(mmu, registers)
    execDispatch = ExecutionUnit.ExecutionDispatcher(mmu, registers)
    writebackDispatch = Writeback.Dispatcher(mmu, registers)
    decoder = Decoder.Decoder()

    cpu = Dispatch.Dispatcher(decoder, addrDispatch, execDispatch, writebackDispatch, mmu, registers)

    cpu.reset()

    while True:
        cpu.dispatch(flagTrace=True, throttleSecs=0.1)

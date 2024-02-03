import sys
import select
import termios
import time
import tty

from Devices.DeviceBase import DeviceBase


class ST16C550(DeviceBase):

    def __init__(self, baseAddress):

        super().__init__(baseAddress, 8)

        self.fd = sys.stdin.fileno()
        self.termios_settings = termios.tcgetattr(self.fd)
        self.poller = select.poll()
        self.poller.register(self.fd, select.POLLIN)
        tty.setraw(self.fd)
        self.ts = 0

        self.RHR = 0
        self.THR = 0
        self.FCR = 0
        self.IER = 0
        self.ISR = 0x01
        self.LCR = 0
        self.LSB = 0
        self.LSR = 0x60
        self.MCR = 0
        self.MCR = 0
        self.MSB = 0
        self.SPR = 0

    def __del__(self):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.termios_settings)

    def readByte(self, address):

        address -= self.baseAddress
        if address == 0x00:
            if self.LCR & 0x80:
                byte = self.LSB
            else:
                fdList = self.poller.poll(0)
                if len(fdList) > 0:
                    self.RHR = ord(sys.stdin.read(1))
                byte = self.RHR
        elif address == 0x01:
            if self.LCR & 0x80:
                byte = self.MSB
            else:
                byte = self.IER
        elif address == 0x02:
            byte = self.ISR
        elif address == 0x03:
            byte = self.LCR
        elif address == 0x04:
            byte = self.MCR
        elif address == 0x05:
            newTs = time.perf_counter_ns()
            if (newTs - self.ts) < 100000:  # Prevent tight loops from hogging host CPU
                time.sleep(.01)
            self.ts = newTs
            fdList = self.poller.poll(0)
            if len(fdList) > 0:
                self.LSR |= 0x01
            else:
                self.LSR &= ~0x01
            byte = self.LSR | 0x20  # Assume THR always ready
        elif address == 0x06:
            byte = self.MSR
        else:
            byte = self.SPR
        return byte

    def writeByte(self, address, byte):

        address -= self.baseAddress
        if address == 0x00:
            if self.LCR & 0x80:
                self.LSB = byte
            else:
                sys.stdout.write(chr(byte))
        elif address == 0x01:
            if self.LCR & 0x80:
                self.MSB = byte
            else:
                self.IER = byte
        elif address == 0x02:
            self.FCR = byte
        elif address == 0x03:
            self.LCR = byte
        elif address == 0x04:
            self.MCR = byte
        elif address == 0x05:
            pass
        elif address == 0x06:
            pass
        else:
            self.SPR = byte

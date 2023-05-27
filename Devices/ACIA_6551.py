import sys
import select
import termios
import time
import tty

import DeviceBase


class ACIA_6551(DeviceBase.DeviceBase):

    def __init__(self, baseAddress):

        super().__init__(baseAddress, 4)
        self.fd = sys.stdin.fileno()
        self.termios_settings = termios.tcgetattr(self.fd)
        self.poller = select.poll()
        self.poller.register(self.fd, select.POLLIN)
        tty.setraw(self.fd)
        self.command = 0x02
        self.control = 0x00
        self.rxdata = 0x00
        self.ts = 0

    def __del__(self):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.termios_settings)

    def readByte(self, address):

        address -= self.baseAddress
        if address == 0:  # Receive Data Register
            fdList = self.poller.poll(0)
            if len(fdList) > 0:
                self.rxdata = ord(sys.stdin.read(1))
            return self.rxdata
        elif address == 1:  # Status Register
            newTs = time.perf_counter_ns()
            if (newTs - self.ts) < 100000:  # Prevent tight loops from hogging host CPU
                time.sleep(.01)
            self.ts = newTs
            fdList = self.poller.poll(0)
            status = 0x10
            if len(fdList) > 0:
                status |= 0x88
            return status
        elif address == 2:  # Command Register
            return self.command
        else:  # Control Register
            return self.control

    def writeByte(self, address, value):

        address -= self.baseAddress
        if address == 0:  # Transmit Data Register
            sys.stdout.write(chr(value))
        elif address == 1:  # Status Register
            pass
        elif address == 2:  # Command Register
            self.command = value
        else:  # Control Register
            self.control = value

This is an emulation of a BBC Micro in Python. Well, mainly it's an emulation
of a 6502 CPU, booting a MOS1.2 ROM image with enough supporting hardware
emulation to get to the BASIC prompt.

There's no keyboard or display emulation as yet - at the moment, output is done
by hooking the `OS_WRCH` syscall and printing the contents of the A register
to `stdout`. The emulator will essentially hang when it gets to an `OS_RDCH`
as it's waiting for a keypress that will never come.

To run the emulator, run `python PyBeeb.js`.

I've tested it with Python 2.7; it won't work with Python 3, I'm afraid.

It's possible to replace parts of the CPU with custom implementations; for
example, see `Dissassembler.py` for an example of how to replace the execution
unit to turn the emulator into a disassembler.

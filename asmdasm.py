#!/usr/bin/python

import sys
from pwn import *
import binascii

tag = str(sys.argv[1])
input2 = sys.argv[2]

if tag.upper() == "ASM":
    instruction = binascii.unhexlify(input2)
    print disasm(instruction,offset=False,byte=False)


if tag.upper() == "DASM":
    asmm = input2 
    print repr(asm(asmm))

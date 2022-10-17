from pwn import *

context.log_level = 'DEBUG'

exe = ELF('<EXE>')
libc = ELF('<LIBC>')
ld = ELF('<LD>')

if args.REMOTE:
    p = remote(host, port)
else if args.DEBUG:
    p = gdb.debug([exe.path, ld.path], env={'LD_PRELOAD': libc.path})
else:
    p = process([exe.path, ld.path], env={'LD_PRELOAD': libc.path})

#### helper functions ####

def one_gadget(filename, base_addr=0):
    return [(int(i)+base_addr) for i in subprocess.check_output(['one_gadget', '--raw', '-10', filename]).decode().split(' ')]

#### shortcut functions ####

sl = lambda x : p.sendline(x)
sla = lambda x, y: p.sendlineafter(x,y)
se = lambda x : p.send(x)
sa = lambda x,y : p.sendafter(x,y)
ru = lambda x : p.recvuntil(x)
rl = lambda : p.recvline()
cl = lambda : p.clean()
uu64 = lambda x : u64(x.ljust(8, b"\x00"))

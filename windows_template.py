import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def p32(x):
    return struct.pack("<I", x)

def p64(x):
    return struct.pack("<Q", x)

def u32(x):
    return struct.unpack("<I", x)[0]

def u64(x):
    return struct.unpack("<Q", x)[0]

uu64 = lambda x : u64(x.ljust(8, b"\x00"))

## exploit ##

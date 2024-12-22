import hashlib
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long
from random import randint
from pwn import xor

cipher="57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637"

print(int.from_bytes(bytes.fromhex(cipher)))
print(long_to_bytes(int(cipher, 16)))
print(bytes.fromhex(cipher))
c=bytes.fromhex(cipher)

randomcheck= [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

flag_check="picoCTF{"
while True: 
    for i in randomcheck:
        for index in range(randint(0, pow(2,0))):
            c=xor(c, i)
    # key=xor(c[:len(flag_check)], flag_check)
    # if key.decode().isprintable():
    #     print(key)
    #     break
    key=b'Africa!A'
    if xor(c, key).startswith(b'picoCTF{') or xor(c, key[:len(key)-1]).startswith(b'picoCTF{') :
        print(xor(c, key))
        print(xor(c, key[:len(key)-1]))
        break
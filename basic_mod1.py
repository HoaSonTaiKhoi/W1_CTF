from string import ascii_uppercase
from string import digits
from pwn import *
import hashlib


list=ascii_uppercase[:]
list+=digits[:]
list+="_"

f=open("C:\\Code C\\Python_Hash\\public\\message.txt", "r").read()
list_encrypted=f.split()

answer=""
for i in list_encrypted:
    answer+= list[int(i)%37]

print(answer)
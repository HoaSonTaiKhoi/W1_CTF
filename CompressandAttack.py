from pwn  import *

import string

r=remote("mercury.picoctf.net", 29858)
list=string.ascii_letters+string.digits+"_}"

answer="picoCTF{"

while "}" not in answer:
    fit=''
    fit_len=999
    for i in list:
      try:
        r.recvuntil("encrypted:")
        r.sendline(answer+i)
        r.recvline()
        r.recvline()
        length=int(r.recvline().decode().rstrip())
        if(length<fit_len):
            fit=i
            fit_len=length
      except:
        r=remote("mercury.picoctf.net", 29858)
    answer+=fit
    print(answer)

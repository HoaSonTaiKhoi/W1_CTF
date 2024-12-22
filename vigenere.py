from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
import hashlib
f=open("C:\Code C\Python_Hash\public\Vigenere_cipher.txt", "r").read()
f=list(f)
key="CYLAB"
n=len(key)

temp=0
for i in range(len(f)):
    if f[i]>='a' and f[i]<='z':
        c=ascii_lowercase.index(f[i])
        e=ascii_uppercase.index(key[temp%n])
        if(c<e):
            f[i]=ascii_lowercase[c+26-e]
        else:
            f[i]=ascii_lowercase[c-e]
        temp+=1
    elif f[i]>='A' and f[i]<='Z':
        c=ascii_uppercase.index(f[i])
        e=ascii_uppercase.index(key[temp%n])
        if(c<e):
            f[i]=ascii_uppercase[c+26-e]
        else:
            f[i]=ascii_uppercase[c-e]
        temp+=1
print(''.join(f))
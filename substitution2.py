import hashlib
from string import ascii_lowercase
from string import ascii_uppercase

f=open("C:\Code C\Python_Hash\public\substitution2.txt", "r").read()

encrypted_letter="nafvptrxesxzqZNVwhyglbckuo"
decrypted_letter="theflagispicoCTFuyrmndkbvx"

list1=dict(zip(encrypted_letter.lower(), decrypted_letter.lower()))
list2=dict(zip(encrypted_letter.upper(), decrypted_letter.upper()))

print(f+"\n")

answer=""
for i in f:
    if i in encrypted_letter.lower() or i in encrypted_letter.upper():
        if i>='a' and i<='z':
            answer+=list1[i]
        elif i>='A' and i<='Z':
            answer+=list2[i]
    else:        
        answer+=i
        
print(answer)
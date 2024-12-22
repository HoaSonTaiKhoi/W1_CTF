import hashlib
from string import ascii_uppercase
from string import digits

list=" "

list +=ascii_uppercase[:]
list += digits
list +="_"
list+="   "

print(list)
f=open("C:\\Code C\\Python_Hash\\public\\message_basic_mod2.txt", "rb").read().split()

phi=41-1
answer=""

def inverse_modulo(a,n):
    return int(pow(a, n-2, n))
for i in f:
    answer+=list[inverse_modulo(int(i), 41)]

print(answer)
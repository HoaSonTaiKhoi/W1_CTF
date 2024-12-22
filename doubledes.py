import itertools
import string
from Crypto.Cipher import DES
import binascii

def pad(m):
    pad=8-len(m)%8
    return (m + " "*pad).encode()

msg="hehe"

key_list=list(itertools.product(string.digits, repeat=6))

for i in range(len(key_list)):
    key_list[i]=DES.new(pad("".join(key_list[i])), DES.MODE_ECB)

enc_msg=binascii.unhexlify("b1151b513009f063c0188357d94cdd75f53c0b879e617fcc9f79593a52581bf023432baee6228089")
test_input=pad("A")
enc_input=binascii.unhexlify("e0ee1e3844ea7efc")

my_dict={}
for i in key_list:
    enc_m=i.encrypt(test_input)
    my_dict[enc_m]=i
       
for i in key_list:
    dec_m=i.decrypt(enc_input)
    if dec_m in my_dict:
        cipher1=my_dict[dec_m]
        answer=cipher1.decrypt(i.decrypt(enc_msg))
        break
print(answer)
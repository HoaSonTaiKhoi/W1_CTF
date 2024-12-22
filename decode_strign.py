import string

LOWERCASE_OFFSET = ord("a")

ALPHABET = string.ascii_lowercase[:16]



encrypted_flag="lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
# key=input("Key")

def decode(b, a):
    enc=""
    binary="{0:04b}".format(ALPHABET.index(b))
    enc+=binary
    binary="{0:04b}".format(ALPHABET.index(a))
    enc+=binary
    
    # print(enc," ", ALPHABET.index(b), " ", ALPHABET.index(a))
    return chr(int(enc, 2))
    
def unshift(c1, c2):
    t1=ALPHABET.index(c1)
    t2=ord(c2) - LOWERCASE_OFFSET
    # print(t1, " ", t2)
    if(t1>=t2):
        return chr(t1-t2+LOWERCASE_OFFSET)
    else:
        return chr(t1+16-t2+LOWERCASE_OFFSET) 

for key in string.ascii_lowercase:
    b16=""
    flag=""
    for i,c in enumerate(encrypted_flag):
        b16 += unshift(c, key[i%len(key)])
        
    # print(b16, " ", len(b16))

    while len(b16) > 0:
        a=b16[0]
        b16=b16[1:]
        b=b16[0]
        b16=b16[1:]
        flag+=decode(a,b)


    print(flag, " ", len(flag))
    

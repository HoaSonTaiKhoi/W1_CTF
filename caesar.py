from string import ascii_lowercase

i=1
a="dspttjohuifsvcjdpoabrkttds"
while i<=25:
    answer=""
    for c in a:
        answer+=ascii_lowercase[(ascii_lowercase.index(c)+i)%26]
    print(answer)
    i+=1
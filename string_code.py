from string import ascii_uppercase as uppercase

number=[16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']

flag=[]

for i in number:
    if type(i)==str:
        flag.append(i)
    else:
        flag.append(uppercase[i-1])

print(''.join(flag))
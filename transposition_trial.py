import hashlib

s="heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"

list=[]
i=0
while i<len(s):
    list.append(s[i:i+3])
    i+=3
    
for i in range(len(list)):
    temp=list[i][2:]+list[i][:2]
    list[i]=temp
    
print (''.join(list))
import hashlib
from string import ascii_lowercase
from string import ascii_uppercase

S="OHNFUMWSVZLXEGCPTAJDYIRKQB"
s=S.lower()

sample="wex dqar bg: cbzjZWD ftipsvhmyln"
new_S="the flag is: picoCTF rbmuynwdvqk"
# list1=dict(zip(s, ascii_lowercase))
# list2=dict(zip(S, ascii_uppercase))
list1=dict(zip(sample, new_S))
list2=dict(zip(sample.upper(), new_S.upper()))

f=open("C:\Code C\Python_Hash\public\substitution1.txt", "r").read()
encrypted_message="Djf webg cfjtqxi, wex dqar bg: cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}"

print(encrypted_message)
answer=""
for i in encrypted_message:
    if i in sample or i in sample.upper():
        if i>='a' and i<='z':
            answer+=list1[i]
        else:
            answer+=list2[i] 
    else:
        answer+=i

print(answer)

# print(f)
# print("\n")
# answer=""
# for i in f:
#         if(i>='a' and i<='z'):
#             answer+=list1[i]
#         elif i>='A' and i<='Z':
#             answer+=list2[i]
#         else:
#             answer+=i
# print(answer)
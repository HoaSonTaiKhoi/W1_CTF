import hashlib
alphabet = "n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy"

assert len(alphabet)== pow(6,2)
matrix = []
for i, letter in enumerate(alphabet):
                if i % 6 == 0:
                    row = []
                row.append(letter)
                if i % 6 == (6 - 1):
                    matrix.append(row)
def get_index(i, matrix):
    for row in range(6):
        for col in range(6):
            if(i== matrix[row][col]):
                return (row, col)
    exit()
    
def fix(index):
    if(index>=1):
        return (index-1)%6
    else:
        return (index+6-1)%6
    
def decrypt_pair(pair, matrix):
    p1=get_index(pair[0], matrix)
    p2=get_index(pair[1], matrix)
    
    if p1[0]==p2[0]:
        return matrix[p1[0]][fix(p1[1])]+ matrix[p2[0]][fix(p2[1])]
    elif p1[1]==p2[1]:
        return matrix[fix(p1[0])][p1[1]]+ matrix[fix(p2[0])][p2[1]]
    else:
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]
    
# for row in range(6):
#     for col in range(6):
#         print(matrix[row][col], end='')
#     print("")

encrypted_msg="hnjm2e4t51v16gsg104i4oi9wmrqli"
msg=""

for i in range(0,len(encrypted_msg),2):
    msg+=decrypt_pair(encrypted_msg[i:i+2], matrix)
    print(msg)

print(msg)
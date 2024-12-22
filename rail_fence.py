
s="*Ta _7N6DDD*hlg:W3D_H3C31N__0D3*ef sHR053F38N43D0F* i33___NA"
n=4
L=len(s)
print(L)
k=L//(2*(n-1))
list=[]

for i in range(0,4):
    if i!=0:
        a=k*(2*i-1)
    else:
        a=0
    if i!=n-1:
        b=k+2*k*i
    else:
        b=len(s)
    list.append(s[a:b])

print(list)
matrix=['']*n
for i in range (n):
    matrix[i]=['']*L

for i in range(n):
    if i==0:
        for j in range(len(list[i])):
            matrix[i][j*(2*n-2)]=list[i][j]
    elif i==n-1:
        for j in range(len(list[i])):
            matrix[i][(n-1)+j*(2*n-2)]=list[i][j]
    else:
        for j in range(len(list[i])):
            if j==0:
                matrix[i][j+i]=list[i][0]
            else:
                matrix[i][i+(2*n-2)*((j-1)//2+1) -(j%2)*2*i]=list[i][j]


f=0
answer=""
for j in range(L):
    answer+=str(matrix[f][j])
    f+=pow(-1, (j//(n-1))%2)

print(answer)
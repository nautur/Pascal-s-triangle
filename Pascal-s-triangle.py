import math

n = 6
triganle = []
for i in range(1,n+1):
    lst = [1]
    for  k in range(i):
        lst.append(1)
    triganle.append(lst)
    if i == 0:
        continue
    else:
        for j in range(1,i//2+1):
            triganle[i-1][j] = triganle[i-2][j]+triganle[i-2][j-1]
            if j != i-j:
                 triganle[i-1][i-j]=triganle[i-1][j]
print(triganle)

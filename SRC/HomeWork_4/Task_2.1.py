z = [2,7,11,15]
x = 9
for i in range(0,len(z)-1):
    for j in range(i+1,len(z)):
        if z[i]+z[j] == x:
            print(i,j)
z1 = [3,2,4]
X1 = 6
for i in range(0,len(z1)-1):
    for j in range(i+1,len(z1)):
        if z1[i]+z1[j] == X1:
            print(i,j)
z2 = [3,3]
X2 = 6
for i in range(0,len(z2)-1):
    for j in range(i+1,len(z2)):
        if z2[i]+z2[j] == X2:
            print(i,j)
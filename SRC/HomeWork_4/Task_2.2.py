z = [2,7,11,15]
x = 9
for i in range(0,len(z)):
    for j in range(i+1,len(z)):
        if z[i]+z[j] == x:
            print(i,j)
z = [2,3,5,6]
x = 9
ind = []
for i in range(0,len(z)):
    for j in range(0,len(z)):
        if z[i]+z[j] == x:
            ind.append(i)
            ind.append(j)
print(ind)
            
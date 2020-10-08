a=(1, 2, 3, 4, 5, 6, 7, 8, 9, 0,)
c=[]
for i in range(0,len(a)):
    if i%2==0:
        c.append(a[i]*2)
    else:
        c.append(a[i]-2)
print(tuple(c))
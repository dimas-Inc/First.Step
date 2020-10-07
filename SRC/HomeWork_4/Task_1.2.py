a = [3, 10, 5, 25, 2, 8]
z=[]
for i in a: 
    b = i^a[0],i^a[1],i^a[2],i^a[3],i^a[4],i^a[5]
    z.append(b)
    m=max(z)
print(max(m))
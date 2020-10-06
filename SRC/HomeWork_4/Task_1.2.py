s=[3, 10, 5, 25, 2]
z=[]
for i in s:
    a=i^s[0]
    z.append(a)
    b=i^s[1]
    z.append(b)
    c=i^s[2]
    z.append(c)
    d=i^s[3]
    z.append(d)
    e=i^s[4]
    z.append(e)
print(max(z))
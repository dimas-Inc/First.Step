z = [6,3,5,8]
x = 9
f =[]
for i in range(0,len(z)):
    if z[0]+z[i] == x:
        print(i,0)
    elif z[1]+z[i]==x:
        print(1,i)
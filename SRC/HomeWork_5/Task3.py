FriendsAndCash =  {'John': 20, 'Dan': 30, 'Lois': 14, 'Doug': 144}
new_FriendsAndCash = {}
total = 0

for v in FriendsAndCash.values():
    total+=v
print('Total money we have is',total,"$")
m = max(FriendsAndCash, key=FriendsAndCash.get)
print(m, FriendsAndCash[m]) 
for i, v in FriendsAndCash.items():
    new_FriendsAndCash[v] = i
print(new_FriendsAndCash)
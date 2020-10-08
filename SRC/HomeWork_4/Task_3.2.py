A = [1,3,4,4,2]
counter = {}
for i in A:
    counter[i] = counter.get(i, 0) + 1
doubles = {element: count for element, count in counter.items() if count > 1}
print(doubles)
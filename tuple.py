t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11,13,15)
l1 = []
l2 = []
#print two different tuples
for i in range(len(t1)):
    if i < len(t1)/2:
        l1.append(t1[i])
    elif i >= len(t1)/2:
        l2.append(t1[i])

print(tuple(l1))
print(tuple(l2))

#even numbers tuple
l3 = []
for x in t1:
    if x%2 == 0:
        l3.append(x)
print(tuple(l3))

#concat t2 with t1
list_1 = list(t1)
list_2 = list(t2)
list_3 = list_1 + list_2
print(tuple(list_3))

#max and min value
print(max(t1))
print(min(t2))

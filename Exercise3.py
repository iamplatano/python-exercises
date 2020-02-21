
a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
i=0
while i<len(a):
    if a[i]<10:
        b.append(a[i])
    i += 1
print(b)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []
for i in range (0,len(a)):
    if a[i] in result:
        i +=1

    for j in range (0,len(b)):
        if a[i] == b[j]:
            result.append(a[i])
print(result)

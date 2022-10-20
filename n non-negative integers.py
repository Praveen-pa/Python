a=list(input("Array =").split())
b=([int(i) for i in a])
area=0
for i in range(len(b)) :
    for j in range(i + 1,len(b)) :
        area = max(area, min(b[j], b[i]) * (j - i))
print(area)

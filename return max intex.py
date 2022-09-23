a=list(map(int,input("nums =").split()))
max=a[0]
index=0
for i in range(1,len(a)):
    if a[i]>max:
        max = a[i]
        index = i
print("Index of the maximum value is :",index)

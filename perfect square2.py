r=int(input())
a=[]
for i in range(1, r + 1):
    if (i**(.5) == int(i**(.5))):
        a.append(i)
print(len(a))

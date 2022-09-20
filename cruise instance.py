E=[]
L=[]
T=int(input("range T:"))
for i in range(T):
    e=int(input("E:"))
    E.append(e)
for i in range(T):
    l=int(input("L:"))
    L.append(l)
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("output",Max)

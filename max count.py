t=int(input("T="))
if t>0:
    e=[]
    l=[]
    for i in range(t):
        e1=int(input("E="))
        e.append(e1)
    for i in range(t):
        l1=int(input("L="))
        l.append(l1)
        sum=0
        v=[]
    for i in range(t):
        sum += e[i]-l[i]
        v.append(sum)
    print(max(v))
else:
    print("INVALID")

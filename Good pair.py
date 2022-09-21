def num(a):
    res=0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if(a[i]==a[j]):
                res+=1
    return res
b=int(input("Enter length of list:"))
n=[]
for i in range(0,b):
    c=int(input("Enter element one by one :"))
    n.append(c)
print("LIST:",n)
print(num(n))

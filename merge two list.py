l1=[1,3,4,2,4]
l2=[2,7,6,5,2,8,4,5]
a=max(len(l1),len(l2))
b=min(len(l1),len(l2))
v=[]
for i in range(0,b):
  v.append(l1[i])
  v.append(l2[i])
for i in range(b,a):
  v.append(l2[i])
print(v)

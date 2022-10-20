s1=input("s1=")
s2=input("s2=") 
d1={}
d2={}
for i, value in enumerate(s1):
    d1[value] = d1.get(value,[])+[i]
for j, value in enumerate(s2):
    d2[value] = d2.get(value,[])+[j]
if sorted(d1.values()) == sorted(d2.values()):
    print("True")
else:
    print("False")

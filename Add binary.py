A=input("a=")
B=input("b=")
p=set(A)
x=set(B)
s={'0','1'}
if s == p or p == {'0'} or p == {'1'} and s ==x or x == {'0'} or x == {'1'} :
    A=int(A,2)
    B=int(B,2)
    c=bin(A+B)
    d=c[2:]
    print(d)
else:
    print("Enter only 0 or 1 ")

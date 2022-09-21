A=int(input("a="),2)
B=int(input("b="),2)
if A == 0 or 1 and B == 0 or 1 :
  c=bin(A+B)
  d=c[2:]
  print(d)
else:
  print("Enter only 0 or 1 ")

A=int(input("a="),2)
B=int(input("b="),2)
if a == 0 or 1 and b == 0 or 1 :
  c=bin(A+B)
  d=c[2:]
  print(d)
else:
  print("Enter only 0 or 1 ")

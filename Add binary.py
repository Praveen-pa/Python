A=int(input("a="))
B=int(input("b="))
C= bin(A + B)
if A > 1 or B > 1:
    print("Enter only 0 or 1 ")
else:
    print(C[2:])

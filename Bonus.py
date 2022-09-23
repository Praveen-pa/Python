a=input("Enter the Grade of the employee:")
b=int(input("Enter the employee salary:"))
bo=0
if a=='A' and b>=10000:
    bo=5/100*b
elif a=='B' and b>=10000:
    bo=10/100*b
elif a=='A' and b<10000:
    bo=7/100*b
elif a=='B' and b<10000:
    bo=12/100*b
print("salary=",b)
print("Bonus=",bo)
print("Total to be paid:",b+bo)

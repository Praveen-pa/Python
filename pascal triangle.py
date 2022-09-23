from math import factorial
n=int(input("Enter the number of rows :"))
a=int(input("Enter the row number :"))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
# nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
    print()
b = 0
for row in range(a):
    b =(1<<row)
print(b)

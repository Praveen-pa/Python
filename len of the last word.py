a=input("Enter the string :")
l=0
x=a.strip()
for i in range(len(x)):
    if x[i]==" ":
        l=0
    else:
        l+=1
print("The length of last word is",l)

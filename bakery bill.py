a=int(input("Enter the Number of new loaves purchased : "))
b=int(input("Enter the Number of old loaves purchased : "))
c=(185-(0.6*185))*b
d=185*a
print("Regular Price : Rs. 185")
print("Old loaves Amount : Rs. ",c)
print("New loaves Amount : Rs. ",d)
print("Total Amount : Rs. ",c+d)

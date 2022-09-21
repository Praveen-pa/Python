from itertools import permutations
nums = []
a=int(input("Enter the size of list :"))
for i in range(0,a):
    b=int(input("Enter the element :"))
    nums.append(b)
perm = permutations(nums) 
for i in list(perm): 
    print (i)
 

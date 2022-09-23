a=int(input("Enter the lenth :"))
(nums,ans) = ([],[])
for i in range(0,a):
    b=int(input("Enter the elements :"))
    nums.append(b)
l=len(nums)
count=0
for i in nums:
    for j in range(l):
        if (nums[j]-i)<0:
            count+=1
    ans.append(count)
    count=0
print(ans)

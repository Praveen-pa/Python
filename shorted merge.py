l1 = []
l2 = []
a=int(input("Enter the size of list 1 :"))
for i in range(0,a):
  print("Enter element for list1: ")
  s = input()
  l1.append(int(s))
b=int(input("Enter the size of list 2 :"))
for j in range(0,b):
  print("Enter element for list2: ")
  s = input()
  l2.append(int(s))
l1.extend(l2)
l1.sort()
print(l1)

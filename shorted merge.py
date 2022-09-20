l1 = []
l2 = []

print("Enter element for list1: ")
while True:
  s = input()
  if s == '*':
    break
  else:
    l1.append(int(s))

print("Enter element for list2: ")
while True:
  s = input()
  if s == '*':
    break
  else:
    l2.append(int(s))

l1.extend(l2)
l1.sort()
print(l1)

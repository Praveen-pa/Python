n=[]
maxi = 0
while True:
  s = input("Sentence =")
  if s=='*':
    break
  else:
    n.append(s)
for i in n:
  s = i.split()
  maxi = max(maxi,len(s))
print(maxi)

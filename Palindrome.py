def ispalindrome(s) :
  rev=''.join(reversed (s))
  if (s==rev):
    return True
  return False
s-input ("X=")
ans- ispalindrome (s)
if (ans):
  print ("true")
else:
  print ("false")

def isPalindrome(s):
    s1 = s.replace(' ', '')
    s1 = s1.lower()
    s2 = s1[::-1];
    return True if s1 == s2 else False
s = input("s=")
if (isPalindrome(s)):
    print ("True")
else:
    print ("False")

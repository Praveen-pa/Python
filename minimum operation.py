def a(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m-1] == s2[n-1]:
        return a(s1, s2, m-1, n-1)
    return 1+min(a(s1, s2, m, n-1),a(s1, s2, m-1, n),a(s1, s2, m-1, n-1))
s1=input("Enter first string:")
s2=input("Enter second string:")
print (a(s1,s2,len(s1),len(s2)))

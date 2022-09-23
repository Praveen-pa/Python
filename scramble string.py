def isScramble(S1: str, S2: str):
    if len(S1) != len(S2):
        return False
    n = len(S1)
    if not n:
        return True
    if S1 == S2:
        return True
    if sorted(S1) != sorted(S2):
        return False
    for i in range(1, n):
       if (isScramble(S1[:i], S2[:i])and isScramble(S1[i:], S2[i:])):
            return True
       if (isScramble(S1[-i:], S2[:i])and isScramble(S1[:-i], S2[i:])):
            return True
    return False
if _name_== "_main_":
    S1 = input("enter the string1:")
    S2 = input("enter the string2:")
    if (isScramble(S1, S2)):
        print("Yes")
    else:
        print("No")

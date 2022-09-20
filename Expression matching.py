import re
s = input("s=")
p = input("p=")
p = r"{}".format(p)
p = re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")

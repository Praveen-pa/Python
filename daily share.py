import sys
c=list(input("Arr =").split())
a=([int(i) for i in c])
b=len(a)
buy1 = -sys.maxsize
sell1 = 0
buy2 = -sys.maxsize
sell2 = 0
for i in range(b):
    buy1 = max(buy1,-a[i])
    sell1 = max(sell1, buy1 + a[i])
    buy2 = max(buy2, sell1 - a[i])
    sell2 = max(sell2, buy2 + a[i])
print(sell2)

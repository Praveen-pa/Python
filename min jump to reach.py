def minJumps(arr, l, h):
	if (h == l):
		return 0
	if (arr[l] == 0):
		return float('inf')
	min = float('inf')
	for i in range(l + 1, h + 1):
		if (i < l + arr[l] + 1):
			jumps = minJumps(arr, i, h)
			if (jumps != float('inf') and
					jumps + 1 < min):
				min = jumps + 1

	return min
arr = []
a=int(input("Enter the size of the list :"))
for i in range(0,a):
        s=int(input("Enter the element :"))
        arr.append(s)
n = len(arr)
print('Minimum number of jumps to reach','end is', minJumps(arr, 0, n-1))

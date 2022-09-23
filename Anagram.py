from collections import defaultdict
test_list = [input()]

print("The original list : " + str(test_list))

temp = defaultdict(list)
for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())

print("The grouped Anagrams : " + str(res))

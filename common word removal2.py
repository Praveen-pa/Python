from collections import Counter
s1 = list(input("Sentence 1 = ").split())
s2 = list(input("Sentence 2 = ").split())
(f1,f2) = (Counter(s1),Counter(s2))
w = 0
for i in range(len(s1)):
	if s1[w] in f2.keys():
		s1.pop(w)
		w=w-1
	w+=1	
w = 0
for i in range(len(s2)):
	if s2[w] in f1.keys():
		s2.pop(w)
		w = w-1
	w+=1
print(*s1)
print(*s2)

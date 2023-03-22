from collections import Counter
def removeCommonWords(sent1, sent2):
	sentence1 = list(sent1.split())
	sentence2 = list(sent2.split())
	sent1_copy = sentence1.copy()
	sent2_copy = sentence2.copy()
	word = 0
	for i in range(len(sentence1)):
		if sentence1[word] in sent2_copy:
			sentence1.pop(word)
			word = word-1
		word += 1	
	word = 0
	for i in range(len(sentence2)):
		if sentence2[word] in sent1_copy:
			sentence2.pop(word)
			word = word-1
		word += 1
	print(*sentence1)
	print(*sentence2)
sentence1 = input("Sentence 1 =")
sentence2 = input("Sentence 2 =")
removeCommonWords(sentence1, sentence2)

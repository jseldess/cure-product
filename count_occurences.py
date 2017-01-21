from collections import Counter

word_cnt = Counter()

for line in open('source.txt'):
	words = line.split()
 	for word in words:
 		word_cnt[word] += 1

new_file = open('source_occurences_words.txt', 'w')
new_file.write(str(word_cnt))

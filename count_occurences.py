import re
from collections import Counter

new_f1 = open('source_occurences_words.txt', 'w')
new_f2 = open('source_occurences_lines.txt', 'w')

word_cnt = Counter()
line_cnt = Counter()

for line in open('source.txt'):
	line_cnt[line] += 1
	words = line.split()
 	for word in words:
 		word_cnt[word] += 1

f2.write(str(word_cnt))
f3.write(str(line_cnt))

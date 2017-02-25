import re
from itertools import combinations
from source_unique_words import words

for pattern in combinations(words, 2):
    print pattern
    new_file = open('regex_couplets/' + str(pattern) + '.txt', 'w')
    new_file.write('\n' + str(pattern) + '\n\n')
    lines_seen = set()
    index = 0
    for line in open('source.txt'):
        if index > 1:
            new_file.write('\n')
            index = 0
        if re.search(pattern[index], line) is not None and len(line) < 100:
            if line.lower().strip() not in lines_seen:
                new_file.write(line)
                lines_seen.add(line.lower().strip())
                index += 1

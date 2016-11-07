from source_unique_words import words

def match_lines_by_word():
    for word in words:
        lines_seen = set()
        new_file = open('../match_lines_by_word/' + str(word) + '.txt', 'w')
        new_file.write('\n' + str(word) + '\n\n')
        for line in open('source.txt'):
            if word.lower() in line.lower():
                if line.lower().strip() not in lines_seen:
                    new_file.write(line + '\n')
                    lines_seen.add(line.lower().strip())

match_lines_by_word()

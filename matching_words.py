import re

pattern = ['oo', 'oa', 'au', 'oo', 'oa', 'au', 'ee', 'ai', 'ee', 'ai', 'ee', 'ai', 'ee', 'ai']
f1 = open('source.txt')
f2 = open('/matching_words/' + str(pattern) + 'ml' + '.txt', 'w+')
f3 = open('/matching_words/' + str(pattern) + 'mw' + '.txt', 'w')

def matching_lines():
    lines_seen = set()
    with f1:
        with f2:
            f2.write('\n' + str(pattern) + '\n\n')
            while True:
                for item in pattern:
                    for line in f1:
                        if re.search(item, line) is not None and len(line) < 100:
                            if line.lower().rstrip() not in lines_seen:
                                f2.write(line)
                                lines_seen.add(line.lower().rstrip())
                                break
                    else:
                        return
                f2.write('\n')


def matching_words():
    words_seen = set()
    with f3:
#       for line in open('source.txt'):                                            # match words in f1
        for line in open('/matching_words/' + str(pattern) + 'ml' + '.txt'):     # match words in f2
            for word in line.split():
                for item in pattern:
                    if re.search(item, word) is not None:
                        if word not in words_seen:
                            if re.search('\[', word) is not None:
                                f3.write('\n' + word + ' ')
                                words_seen.add(word)
                            elif re.search('\]', word) is not None:
                                f3.write(word + '\n\n\n')
                                words_seen.add(word)
                            elif re.search('\.|\?|,', word) is not None:
                                f3.write(word + '\n\n')
                                words_seen.add(word)
                            elif re.search('^[A-Z]', word):
                                f3.write('\n\n' + word + ' ')
                                words_seen.add(word)
                            else:
                                f3.write(word + ' ')
                                words_seen.add(word)

matching_lines()
matching_words()





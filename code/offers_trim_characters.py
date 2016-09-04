import re

pattern = ['without', 'without']
f1 = open('source.txt')
f2 = open('../common_measure/' + str(pattern) + 'trimmed' + '.txt', 'w')


def trim_characters():
    lines_seen = set()
    with f1:
        with f2:
            f2.write('\n' + str(pattern) + '\n\n')
            while True:
                for item in pattern:
                    for line in f1:
                        if re.search(item, line) is not None and len(line) < 100:
                            if line not in lines_seen:
                                lines_seen.add(line)
                                trimmed = ' '.join([s[1:-1] for s in line.split(' ')])
                                f2.write(trimmed)
                                break
                    else:
                        return
                f2.write('\n')

trim_characters()

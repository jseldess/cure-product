import re

def match_lines_by_regex():
    pattern = ['A', 'across']
    new_file = open(str(pattern) + '.txt', 'w')
    new_file.write('\n' + str(pattern) + '\n\n')
    lines_seen = set()
    while True:
        for item in pattern:
            for line in open('source.txt'):
                if re.search(item, line) is not None and len(line) < 100:
                    if line.lower().strip() not in lines_seen:
                        new_file.write(line)
                        lines_seen.add(line.lower().strip())
                        break
            else:
                return
        new_file.write('\n')

match_lines_by_regex()

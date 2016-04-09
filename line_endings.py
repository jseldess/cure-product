import re

a = "m"
b = "n"
c = "p"
d = "o"
e = "r"
f = "t"
g = "d"

def english_sonnets():
    lines_seen = set()
    f1 = 'source.txt'
    with open('english_sonnets1.txt', 'w') as f2:
        while True:
            for ending in [a, b, a, b, c, d, c, d, e, f, e, f, g, g]:
                for line in open(f1):
                    if re.search('.' + ending + '$', line) is not None and len(line) < 100:
                        if line not in lines_seen:
                            f2.write(line)
                            lines_seen.add(line)
                            break
                else:
                    return

            f2.write('\n')

def italian_sonnets():
    lines_seen = set()
    f1 = 'source.txt'
    with open('italian_sonnets1.txt', 'w') as f2:
        while True:
            for ending in [a, b, b, a, a, b, b, a, c, d, e, c, d, e]:
                for line in open(f1):
                    if re.search('.' + ending + '$', line) is not None and len(line) < 100:
                        if line not in lines_seen:
                            f2.write(line)
                            lines_seen.add(line)
                            break
                else:
                    return

            f2.write('\n')

english_sonnets()
italian_sonnets()
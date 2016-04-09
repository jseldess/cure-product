import re

a = "m"
b = "n"
c = "p"
d = "o"
e = "r"
f = "t"
g = "d"

def sonnets():
    lines_seen = set()
    f1 = 'source.txt'
    with open('sonnets1.txt', 'w') as f2:
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

sonnets()

import re

a = "th"
b = "em"
c = "al"
d = "y"
e = "ere"
f = "o"
g = "en"

def english_sonnets():
    lines_seen = set()
    f1 = '../text/source.txt'
    with open('../sonnets/2english_sonnets.txt', 'w') as f2:
        f2.write('a=' + a + '\n' + 'b=' + b + '\n' + 'c=' + c + '\n' + 'd=' + d + '\n' + 'e=' + e + '\n' + 'f=' + f + '\n' + 'g=' + g + '\n\n')
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
    f1 = '../text/source.txt'
    with open('../sonnets/2italian_sonnets.txt', 'w') as f2:
        f2.write('a=' + a + '\n' + 'b=' + b + '\n' + 'c=' + c + '\n' + 'd=' + d + '\n' + 'e=' + e + '\n\n')
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
import re

a = "th"
b = "em"
c = "al"
d = "y"
e = "ere"
f = "o"
g = "en"

def italian_sonnets():
    lines_seen = set()
    f1 = 'source.txt'
    with open('sonnets.txt', 'w') as f2:
        f2.write('ITALIAN SONNETS:' + ' (a=' + a + ', ' + 'b=' + b + ', ' + 'c=' + c + ', ' + 'd=' + d + ', ' + 'e=' + e + ')\n\n')
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

def english_sonnets():
    lines_seen = set()
    f1 = 'source.txt'
    with open('sonnets.txt', 'a') as f2:
        f2.write('\n' + 'ENGLISH SONNETS:' + ' (a=' + a + ', ' + 'b=' + b + ', ' + 'c=' + c + ', ' + 'd=' + d + ', ' + 'e=' + e + ', ' + 'f=' + f + ', ' + 'g=' + g + ')\n\n')
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


italian_sonnets()
english_sonnets()

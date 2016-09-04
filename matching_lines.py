import re

pattern = ['before', '^stop', 'ce', 're', 'scanned', '^Or.*can\s']
f1 = open('source.txt')
f2 = open('/matching_lines/' + str(pattern) + 'ml' + '.txt', 'w')

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

matching_lines()

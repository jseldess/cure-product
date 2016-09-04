import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

endings = ["or", "re", "al"]

def fuzzy_ending():
    lines_seen = set()
    f1 = open('source.txt')
    with open('/matching_lines/cm25.txt', 'w') as f2:
        f2.write('\n' + 'COMMON MEASURE FUZZY: ' + str(endings) + '\n\n')
        while True:
            for ending in endings:
                for line in f1:
                    if line not in lines_seen and len(line) > 100:
                        match = re.search(re.compile(r'.' + ending + '$'), line)
                        if match is not None and fuzz.partial_ratio(ending, match) > 10:
                            f2.write(line)
                            lines_seen.add(line)
                            break
                else:
                    return
            f2.write('\n')

a = "Where I sleep at times"
b = "and not falling at all"
c = "I had nightmares though"
d = "That is itself not still"
e = "I assume the offers reliable"
f = "We ask say in that case"

def common_measure_fuzzy_line():
    lines_seen = set()
    f1 = open('source.txt')
    with open('/matching_lines/cm_fuzzy(60)_' + f + '_' + f + '.txt', 'w') as f2:
        f2.write('\n' + '[' + f + ', ' + f + ']\n\n')        
        while True:
            for ln in [f, f]:
                for line in f1:
                    if line not in lines_seen and len(line) < 100:
                        if fuzz.partial_ratio(ln, line) > 60:
                            f2.write(line)
                            lines_seen.add(line)
                            break
                else:
                    return
            f2.write('\n')


#common_measure_fuzzy_ending()
common_measure_fuzzy_line()

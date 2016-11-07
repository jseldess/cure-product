import re

def match_lines_by_regex():
    pattern = ['advance', 'ads']
    lines_seen = set()
    new_file = open('../match_lines_by_regex/' + str(pattern) + '.txt', 'w')
    new_file.write('\n' + str(pattern) + '\n\n')
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


# Why does the following not alternate items of the pattern,
# one line with one item, the next line with the other item, etc.?
#
# pattern = ['claim', 'cure']
# new_file = open('../match_lines_by_regex/' + str(pattern) + '2.txt', 'w')
# new_file.write('\n' + str(pattern) + '\n\n')
# lines_seen = set()
# for item in pattern:
#     for line in open('source.txt'):
#         if re.search(item, line) is not None and len(line) < 100:
#             if line.lower().strip() not in lines_seen:
#                 new_file.write(line)
#                 lines_seen.add(line.lower().strip())
#                 if item == pattern[-1]:
#                     new_file.write('\n')
#                     break

import re
import os
import glob

patterns = ['or', 's$']
path = '../common_measure/'
f2 = open('../multisource/' + str(patterns) + '.txt', 'w')

# def multisource():
#     lines_seen = set()
#     for filename in glob.glob(os.path.join(path, '*.txt')):
#         # f1 = filename
#         # print f1
#         # with open(f1):
#         with f2:
#             f2.write('\n' + str(patterns) + '\n\n')
#             while True:
#                 for item in patterns:
#                     for line in filename:
#                         if re.search(item, line) is not None:
#                             if line not in lines_seen:
#                                 f2.write(line)
#                                 lines_seen.add(line)
#                                 break
#                     else:
#                         return
#                 f2.write('\n')

# multisource()


def multisource():
    lines_seen = set()
    for file in os.listdir(path):
        with open(file, 'r'):
            with f2:
                f2.write('\n' + str(patterns) + '\n\n')
                while True:
                    for item in patterns:
                        for line in file:
                            if re.search(item, line) is not None:
                                if line not in lines_seen:
                                    f2.write(line)
                                    lines_seen.add(line)
                                    break
                        else:
                            return
                    f2.write('\n')

multisource()

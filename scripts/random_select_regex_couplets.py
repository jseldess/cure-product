import collections
import glob
import random
import re

# Create a list with filepaths from specified directory.
fpaths = glob.glob('regex_couplets/*.txt')

# Create another list and add just filenames from fpaths.
fnames = list()
for f in fpaths:
	fnames.append(re.findall('\(.*\).txt', f))

# Convert fnames from a list of lists to a list of strings.
fnames = [''.join(x) for x in fnames]
print fnames

# Create a dictionary that maps whatever's to the left of the comma in the 
# filename to the list of fnames. 
d = collections.defaultdict(list)
for f in fnames:
	left = f.split(',')[0]
	d[left].append(f)

# Use random.choice to pick randomly from the list of filenames for each key 
# in the dictionary.
choices = list()
for left in sorted(d.keys()):
    choices.append(random.choice(d[left]))

# Sort the chosen filenames. Copy the contents of each file with more than 
# specified number of lines to a new file.
new_file = open('random_select_regex_couplets/' + '1.txt', 'w')
sorted_choices = sorted(choices, key=lambda s: s.lower())
for choice in sorted_choices:
    num_lines = sum(1 for line in open('regex_couplets/' + choice))
    if num_lines > 18:
		for line in open('regex_couplets/' + choice):
			new_file.write(line)

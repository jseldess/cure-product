import re
import collections
import glob
import random
import os
from itertools import combinations

source = raw_input('Source file: ')
num_files = int(raw_input('# of random selection files to generate: '))

def find_unique_words(source):
	words_seen = []
	for line in open(source):
		words = line.split()
		for word in words:
			if word not in words_seen:
				words_seen.append(str(word))
	words_seen.sort()
	return words_seen

def create_files():
	if not os.path.exists('generated_files'):
		os.makedirs('generated_files')
	for pattern in combinations(find_unique_words(source), 2):
		temp = ''
		temp += '\n' + str(pattern) + '\n\n'
		lines_seen = set()
		index = 0
		line_count = 3
		for line in open(source):
			if index > 1:
				temp += '\n'
				index = 0
			if re.search(pattern[index], line) is not None:
				if line.lower().strip() not in lines_seen:
					temp += line
					lines_seen.add(line.lower().strip())
					index += 1
					line_count += 1
		print pattern, line_count
		if line_count > 7:
			new_file = open('generated_files/' + str(pattern) + '.txt', 'w')
			new_file.write(temp)

def select_files():
	if not os.path.exists('selected_files'):
		os.makedirs('selected_files')
	fpaths = glob.glob('generated_files/' + '/*.txt')
	fnames = list()
	for f in fpaths:
		fnames.append(re.findall('\(.*\).txt', f))
	fnames = [''.join(x) for x in fnames]
	d = collections.defaultdict(list)
	for f in fnames:
		left = f.split(',')[0]
		d[left].append(f)
	choices = list()
	for i in range(num_files):	
		for left in sorted(d.keys()):
		    choices.append(random.choice(d[left]))
		new_file = open('selected_files/' + str(i) + '.txt', 'w')
		sorted_choices = sorted(choices, key=lambda s: s.lower())
		for choice in sorted_choices:
		    num_lines = sum(1 for line in open('generated_files/' + choice))
		    if num_lines > 3:
				for line in open('generated_files/' + choice):
					new_file.write(line)

create_files()
select_files()

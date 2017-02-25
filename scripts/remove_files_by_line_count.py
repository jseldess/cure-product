import os, os.path

# Loop through files in a directory. 
# If a file has less lines than num_lines, remove it.
for root, _, files in os.walk('regex_couplets/'):
    for f in files:
    	print f
        fullpath = os.path.join(root, f)
        num_lines = sum(1 for line in open(fullpath))
        if num_lines < 8:
        	os.remove(fullpath)

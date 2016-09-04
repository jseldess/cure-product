import nltk

# File with words to analyze.
f1 = open('source.txt')
# File with each word and its part of speech, including repetitions.
f2 = open('source_pos_repeat.txt', 'w+')
# File with each word and its part of speech, no repetitions.
f3 = open('source_pos_norepeat.txt', 'w+')

# Identify the pos of every word in source.txt, including repetitions.
def identify_pos_repeat():
    with f1:
        with f2:
        	# Look at each line in f1.
            for line in f1:
            	# Split each line into words. 
                for word in line.split():
                	# Tokenize each word.
                    text = nltk.word_tokenize(word)
                    # Tag each word with its pos.
                    pos = nltk.pos_tag(text)
                    # Write each word with its pos to f2.
                    f2.write(str(pos) + '\n')

# Identify the pos of every unique word in source.txt.
def identify_pos_norepeat():
	# Record each unique word.
    words_seen = set()
    with f1:
        with f3:
        	# Look at each line in f1.
            for line in f1:
            	# Split each line into words.
                for word in line.split():
                	# If word is unique, continue.
                    if word not in words_seen:
                    	# Tokenize each unique word.
                        text = nltk.word_tokenize(word)
                        # Tag each unique word with its pos.
                        pos = nltk.pos_tag(text)
                        # Write each unique word with its pos to f2.
                        f3.write(str(pos) + '\n')
                        # Add each unique word to words_seen.
                        words_seen.add(word)


identify_pos_repeat()
identify_pos_norepeat()

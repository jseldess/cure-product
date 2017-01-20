# Cure Product

This repository contains files used to generate materials for the **BACK UP** sections the book, **CURE PRODUCT**. It's also here to document the basic process I followed, though I ended up at this process only after a lot of experimentation.

## Basic Process

1. I ran `count_occurences.py` on `source.txt` to create `source_occurences_words.txt`, which contains a dictionary counting the occurence of each unique word in `source.txt`. 

2. I converted the dictionary in `source_occurences_words.txt` into a list of unique words without their counts and saved it as `source_unique_words.py`. 

   Note: Although this file now matches the words in `source_occurences_words.txt`, when I used it in step 3, I stripped away words that occurred more than something like 100 times. I can't remember exactly. 

3. I ran `regex_couplets.py` on `source.txt`. 

   Essentially, this script iterated through each unique combination of words in `source_unique_words.py` ("A" and "above", then "A" and "accounting", etc.), using a regular expression search to identify lines containing these sequence of characters (as words or a parts of words) and writing those lines to a new file in the `/regex_couplets` directory. Given the many unique combinations of words in `source_unique_words.py`, this process took awhile.

4. I ran `remove_files_by_line_count.py` to remove any files generated in step 3 with less than a few couplets. 

5. I ran `random_select_regex_couplets.py` to randomly select files from `/regex_couplets` and write them to a new file in `/random_select_regex_couplets`.

   I decided to do random selection because, though step 4 reduced the total file count significantly, the remaining total was still way too high to review manually (I tried for a while). 

6. I read through the resulting random selection and further selected "poems" for inclusion in **CURE PRODUCT**. 

   I didn't use these verbatim. Rather, I gave myself some basic guidelines, again, coming to these after a lot of experimentation. Per poem:
    - Any first line of a couplet could be exchanged with any other first line of a couplet. Same for second lines.
    - Any line could be left out. 

7. I repeated steps 5 and 6 many times.

In addition to the above, I came up with a few poems in the `BACK UP` sections using the `regex_pattern.py` script, which I manually edited to specify the words, parts of words, or text patterns to look for. For example, the poem **^without, ^without** was the result of a regular expression search for lines beginning with the word "without", and the poem **m$, n$, n$, m$** was the result of a regular expression search for lines ending with those letters. 

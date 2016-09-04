import nltk


f1 = open("../matching_words/['will', 'would']ml.txt").read()
tokens1 = nltk.word_tokenize(f1)
text1 = nltk.Text(tokens1)

f2 = open("source.txt").read().decode('utf-8')
tokens2 = nltk.word_tokenize(f2)
text2 = nltk.Text(tokens2)

f3 = open("../similar_lines/['sun'].txt", 'w+')

f3.write(text2.similar(text1))

import nltk

# f1 = open('source.txt')
# f2 = open("../matching_lines/['last', 'ff']ml.txt")
# f3 = open("../similar_lines/['without','without']cm.txt", 'w+')

# text1 = 'A basically stupid sentence.'

# def similar_lines():
# 	with f1:
# 		with f2:
# 			f3.write(text1.similar(f2))

# similar_lines()


# f1 = open('source.txt')
# f2 = open("../matching_lines/['will', 'would']ml.txt")
# f3 = open("../similar_lines/['without','without']cm.txt", 'w+')

# def similar_lines():
#     with f1:
#         with f2:
#             text1 = nltk.word_tokenize(f1)
#             text2 = nltk.word_tokenize(f2)
#             f3.write(text1.similar(text2))

# similar_lines()


f1 = open("../matching_words/['will', 'would']ml.txt").read()
tokens1 = nltk.word_tokenize(f1)
text1 = nltk.Text(tokens1)

f2 = open("source.txt").read().decode('utf-8')
tokens2 = nltk.word_tokenize(word.lower() for word in f2)
text2 = nltk.Text(tokens2)

f3 = open("../similar_lines/['sun'].txt", 'w+')

print text1.similar(text2)

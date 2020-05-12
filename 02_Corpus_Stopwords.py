from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

test_string = "This is an example showing stopwords from corpus in nltk"

# This will store almost all the stop words in english
stop_words = set(stopwords.words("english")) 

words = word_tokenize(test_string)

filtered_sentence = []

for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)

print(filtered_sentence) 
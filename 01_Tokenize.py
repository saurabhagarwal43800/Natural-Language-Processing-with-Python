from nltk.tokenize import word_tokenize, sent_tokenize

# word_tokenize()- seperates the string according to words in a list
# sentence_tokenize()- seperates the string according to sentence in a list

test_string = "Hello, My name is Saurabh. I am a Python developer, DataScientist and a DevOps enthusiast. I like developing and integrating things, what about you?"

print(word_tokenize(test_string))
print(sent_tokenize(test_string))
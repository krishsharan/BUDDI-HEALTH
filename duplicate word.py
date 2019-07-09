import nltk
word_data = open('orig.txt', "w")
nltk_tokens = nltk.word_tokenize(word_data)

ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)

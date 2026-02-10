import nltk
from nltk.util import ngrams


sentence = "Natural language processing with nltk"
n = 4

words = sentence.split()
word_ngrams = ngrams(words, n)

print("Word", n, "-grams:")
for gram in word_ngrams:
    print(gram)

print("\nCharacter", n, "-grams:")

char_ngrams = ngrams(sentence, n)

for gram in char_ngrams:
    print("".join(gram))
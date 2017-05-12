import nltk
from nltk.corpus import gutenberg

print("\n*******************\n")
# access Gutenberg corpus
print(nltk.corpus.gutenberg.fileids())

# get all words of a document
print(len(nltk.corpus.gutenberg.words('austen-emma.txt')))

# statistics for all doc, the average len of word, average len of sentence, and the frequency of word
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

# raw is character stream.
raw = gutenberg.raw('austen-emma.txt')
print(raw[:10])



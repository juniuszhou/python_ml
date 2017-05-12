from nltk.book import *
from nltk import *

# the most import class in nltk is text.
# it is similar to list of words

print("\n*******************\n")
# print book 's name
print(text1.name)
print(text2.name)

print("\n*******************\n")
# search via key word concordance means index and coincidence
# list all context include the monstrous token
print(text1.concordance("monstrous"))

print("\n*******************\n")
# print word in word text1 similar to monstrous
text1.similar("monstrous")

print("\n*******************\n")
# print word in word text1 similar to monstrous
text2.similar("monstrous")

# generate random document. this method seems deprecated.
# text3.generate()

# to show the distribution of several tokens in document.
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])


print("\n*******************\n")
# assistant method can apply to text
print(len(text1))
print(text1.count('the'))
print(len(set(text1)))

# method as a list
print("\n*******************\n")
print(text1[1])
print(text1[0:10])
print(text1.index("the"))

# get each word len
allLens = [len(w) for w in text1]

# get distribution and show it
top100 = text1[0:100]
dis = FreqDist(top100)
print("\n******************* appeared more than once\n")
print([w for w in set(dis) if dis[w] > 2])
## dis.plot()

print("\n*******************\n")
## bi-gram method
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))


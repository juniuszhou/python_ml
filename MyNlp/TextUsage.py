from nltk import *

# get text object from list of words.
text1 = Text(["jun", "red", "jun", "red", "red", "jun", "red", "am"])
print("*******************\n")
print(text1.tokens)

print("*******************\n")
print(" ".join(text1))

print("*******************\n")
print(list(bigrams(text1)))
print(list(ngrams(text1, 3)))

print("*******************\n")
# print frequent sequence. window_size for two words in 5 scope.
print(text1.collocations(window_size=5))

# get distribution. the inner data structure is a list<map>.
# key is token's length, and value is token's number with the length
print("*******************\n")
fdist = FreqDist([len(w) for w in text1])
print(sorted(fdist.keys()))
print(fdist.items())
print(str(fdist.items()[0][0]) + " value is " + fdist.items()[0][1])

# s.startswith(t)	test if s starts with t
# s.endswith(t)	test if s ends with t
# t in s	test if t is contained inside s
# s.islower()	test if all cased characters in s are lowercase
# s.isupper()	test if all cased characters in s are uppercase
# s.isalpha()	test if all characters in s are alphabetic
# s.isalnum()	test if all characters in s are alphanumeric
# s.isdigit()	test if all characters in s are digits
# s.istitle()	test if s is titlecased (all words in s have have initial capitals)
#
print("*******************\n")
for token in text1:
    if token.startswith("r"):
        print(token)


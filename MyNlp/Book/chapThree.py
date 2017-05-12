from __future__ import division
from urllib import urlopen
import nltk, re, pprint


def deal_normal_text():
    url = "http://www.gutenberg.org/files/2554/2554.txt"
    raw = urlopen(url).read()
    print(raw[:50])

    tokens = nltk.word_tokenize(raw)
    print(tokens[:10])

    text = nltk.Text(tokens)
    print(text[:10])

    # print most frequent collocations. gu ding da pei
    print(text.collocations(10))

    print("--------------------")
    # locate string in raw
    print(raw.find("PART I"))
    print("--------------------")


# deal with HTML part.
def deal_html_text():
    url = "http://www.baidu.com"
    html = urlopen(url).read()
    print(html[:40])
    raw = nltk.clean_html(html)
    tokens = nltk.word_tokenize(raw)
    print(tokens[:20])
    text = nltk.Text(tokens)
    text.concordance("baidu")


deal_html_text()

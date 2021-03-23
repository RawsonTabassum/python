import requests
from bs4 import BeautifulSoup
import operator

def start (url):
    wordList = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features = "html.parser")
    for post_text in soup.findAll('a', {'itemprop' : 'url'}):
        content = post_text.string
        #print(content)
        words = content.lower().split()

        for each_word in words:
            #print(each_word)
            wordList.append(each_word)
    cleanup_list(wordList)


def cleanup_list (wordlist):
    cleanList = []

    for word in wordlist:
        symbols = "~!@#$%^&*()_+{}|:<>?\"'[]\;,./-=1234567890"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            #print(word)
            cleanList.append(word)

    create_dictionary(cleanList)


def create_dictionary(cleanList):
    wordCount = {}

    for word in cleanList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    for key, value in sorted(wordCount.items(), key = operator.itemgetter(1)):
        print(key, value)

start("https://www.g7website.com/showcase.html")


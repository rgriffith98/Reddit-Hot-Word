import requests
from bs4 import BeautifulSoup
import operator

###

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll('a', {'data-event-action': 'title'}):
        content = post_text.string
        words = content.lower().split()

        for each_word in words:
            word_list.append(each_word)

    clean(word_list)

#to remove symbols and empty words
def clean(word_list):
    cleaned = []
    for word in word_list:
        symbols = "~!@#$%^&*()_-+=\][}{|/?><."
        for character in range(0, len(symbols)):
            word = word.replace(symbols[character], "")
        if len(word) > 0:
            cleaned.append(word)

    dict(word_list)

def dict(word_list):
    w_count = {}
    for word in word_list:
        if word in w_count:
            w_count[word] += 1
        else:
            w_count[word] = 1
    for key, value in sorted(w_count.items(), key = operator.itemgetter(1)):
        print(key, value)

###

start('https://www.reddit.com')

#note that the program may need to be ran several times to get through reddits low webcrawler acceptance rate
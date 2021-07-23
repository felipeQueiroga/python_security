import sys
from bs4 import BeautifulSoup
from collections import Counter
import operator   # + - * / and not or
import requests 

def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')
    find_list = soup.findAll('div', {'class': 'entry-content'})
    print(find_list)
    for each_text in find_list: 
        content = each_text.text

        words = content.lower().split()
        for each_words in words:
            wordlist.append(each_words)
            print(each_words)
            print(wordlist)
    clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        Symbols = '"!@#$%¨&*()[]{}^<>,.;:/\|*-+_'
        for i in range(0, len(Symbols)):
            word = word.replace(Symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)
    creat_dictionary(clean_list)

def creat_dictionary(clean_list):   
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
  
    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print("% s : % s" % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)

if __name__ == "__main__":
    start("https://www.issqn.net/")
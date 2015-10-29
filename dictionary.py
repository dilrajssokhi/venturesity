#!/usr/bin/python

import requests

r = requests.get("http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt")

dictionary = {}
for word in r.text.split("\r\n"):
    if (len(word) > 0):
        if (dictionary.has_key(str(word[0:2]))):
            dictionary[str(word[0:2])].append(str(word))
        else:
            dictionary[str(word[0:2])] = [str(word)]

print dictionary  

input_word = raw_input().lower()
if (dictionary.has_key(input_word[0:2])):
    search_list = dictionary[input_word[0:2]]
    if input_word in search_list:
        print "The string is a valid word."
    else:
        print "The string is not a valid word."

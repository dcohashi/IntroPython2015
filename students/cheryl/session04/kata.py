#!/usr/bin/env python3
import random
# create a dictionary for the lookup
lookup = dict()
punctuation = set(".,!?")
chars = "-()[]{}*&^%$#@=+\"\n"

# read file
word = ["", "", ""]
with open('input.txt', 'r') as f:
    for line in f:
        # either read entire text at once or figure out how to continue through lines

        # remove the non-alpha
        transtable = line.maketrans('', '', chars)
        wordsonly = line.translate(transtable)

        # make line into a list
        words = wordsonly.split()

        # parse through file and create dictionary with key pointing to a list
        for new_word in words:
            word[0] = word[1]
            word[1] = word[2]
            word[2] = new_word
            # if all words are available
            if word[0] is not None and word[1] is not None:
                # join two words together to make the key
                key = (word[0].lower(), word[1].lower())

                # if key is already in the dictionary append new value to the list
                if key in lookup:
                    lookup[key].append(word[2].lower())
                else:
                    lookup[key] = [word[2].lower()]


# create new text

def next_phrase(phrase, lookup):
    '''
    Use the phrase as keyword lookup then return a random word from the list. Return None if there is no matching phrase.
    '''
    if phrase not in lookup:
        return None
    else:
        # if matching phrase, output a random item from the list
        next_word = random.choice(lookup[phrase])
        return(next_word)

# input starting phrase
f = open('output.txt', 'w', encoding='utf8')
word1 = input('Enter word: ')
f.write(word1.capitalize())
word2 = input('Enter 2nd word: ')
f.write(' '+word2)
caps = False
# lookup next word and write to file
while word2 is not None:
    next_word = next_phrase((word1, word2), lookup)
    if next_word == 'i':
        f.write(' I')
    elif next_word is not None:
        if caps:
            f.write(' '+next_word.capitalize())
            caps = False
        else:
            f.write(' '+next_word)
        if any((c in chars) for c in next_word):
            caps = True
    word1 = word2
    word2 = next_word
else:
    f.close()

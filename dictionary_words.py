# DICTIONARY WORDS
    # All hardcoded parameters
    # Program accepts one argument (number of words)
    # Returns random sentence (does not have to make grammatical sense)

import sys
import random

# Read from this file
file = open("sample_text.txt")

# Select Random Words, Split, and Store in a Data Type
list_of_words = file.read().split(" ")
# Specify number of words you want from sample
random_words = random.choices(list_of_words, k = 6)


# Form Sentence
random_sentence = ' '.join(random_words)
print(random_sentence)



# ANOTHER WAY 
# Word_Count=input("Please enter a number")
# word_list = []
#
# with open("/usr/share/dict/words", "r") as file:
#     while Word_Count < len(word_list):
#         random_num = random.randint(0,len(list_of_words))
#         random_word = list_of_words(random_num)
#         word_list.append(random_word)
#
#     print(''.join(word_list))

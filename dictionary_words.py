import sys
import random

# Program only accepts one arguemnt
# All parameters are hardcoded
# Sentences don't have to make grammatical sense
# Word selection is random

# Read the file
file = open("words.txt")

# Select random words and store in a data type
list_of_words = file.read().split(" ")
randomWords = random.choices(list_of_words, k = 6)

# Don't forget to close file! If you don't use with open()...
file.close()
# Put num of words together
print(list_of_words)

# Print words in a sentence
print(' '.join(randomWords))



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

import sys
import random

# Program only accepts one arguemnt
# All parameters except number of words hardcoded
# Will use words file available on all Unix systems
# Sentences don't have to make grammatical sense
# Word Selection can be random


# Read the file
file = open("words.txt")

# Select random words and store in a data type
list_of_words = file.read().split(" ")
randomWords = random.sample(list_of_words, 6)

# Put num of words together
print(list_of_words)

# Print words in a sentence
print(' '.join(randomWords))

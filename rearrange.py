# This randomly rearranges a set of words provided as commandline arguments (sys.argv)
import sys
import random

def rearrange_words():
    input_words = []
    output_words = []

    for word in sys.argv:
        # remember sys.argv considers file name
        if word != sys.argv[0]:
            input_words.append(word)

    # If there are still words in the list...
    while len(input_words) > 0:
        # items passed randomly
        randomItem = random.randint(0, len(input_words) -1)
        output_words.append(input_words[randomItem])
        input_words.pop(randomItem)

    # return " ".join(output_words)
    print( " ".join(output_words))

if __name__ == '__main__':
    rearrange_words()


# ANOTHER WAY

# sentence = input("Enter a Simple Sentence")
#
# def rearrange_words():
#     input_words = sys.argv[1:]
#     words = []
#     for word in input_words:
#         rand_index = random.randint(0, len(input_words) -1)
#         list = input_words[rand_index]
#         words.append(list)
#         result = ' '.join(words)
#         return result

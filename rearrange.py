import sys
import random

def rearrange_words():
    '''Randomly rearranges set of words provided as commandline arguments (sys.argv)
    '''

    # See bottom example for alternative
    input_words = []
    output_words = []

    for word in sys.argv:
        # Remember sys.argv considers file name
        if word != sys.argv[0]:
            input_words.append(word)

    # If there are still words in the list...
    while len(input_words) > 0:
        # Items passed randomly
        randomItem = random.randint(0, len(input_words) -1)
        output_words.append(input_words[randomItem])
        input_words.pop(randomItem)

    # return " ".join(output_words)
    print( " ".join(output_words))

if __name__ == '__main__':
    rearrange_words()


# ANOTHER WAY

# def rearrange_words():
#     input_words = sys.argv[1:]
#     words = []
#     for word in input_words:
#         rand_index = random.randint(0, len(input_words) -1)
#         list = input_words[rand_index]
#         words.append(list)
#         result = ' '.join(words)
#         return result

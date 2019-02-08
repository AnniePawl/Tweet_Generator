import sys

def reverse_words():
    words = sys.argv[1:]
    output_words =  reverse_words[::-1]

    print( " ".join(output_words))

if __name__ == '__main__':
    reverse_words()

# SAMPLE STRATEGY
# >>> y
# [8, 7, 6, 5, 4, 3, 2, 1, 0]
# >>> x = range(9)
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# >>> y=x[::-1]
# >>> y
# [8, 7, 6, 5, 4, 3, 2, 1, 0]

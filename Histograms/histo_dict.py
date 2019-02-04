# DICTIONARY HISTOGRAM
# Something is wrong?

# READ from this FILE
file = open("../words.txt")

# HISTOGRAM FUNCTION
def histogram(list):
    '''
    Returns unique values and the
    number of occurances of each
    '''
    dict = {}
    for word in list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    print(dict)

if __name__ =='__main__':
    histogram("/..words.txt")

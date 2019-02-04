# LISTS OF LISTS

# READ from this FILE
# file = open("../words.txt")

# READ FROM THIS FILE
def get_word_list(file_name = '../words.txt'):
    '''Gets words, gets rid of nonsense'''
    file = open(file_name,'r')
    read_words = file.readlines()
    # Don't forget to close file!
    file.close()
    words = list()
    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.lower().strip("(),!."""))
    # print(words)

    return words


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

    return(dict)


def list_of_lists(dictionary):
    lol = []
    for thing in dictionary:
        entry = [thing, dictionary[thing]]
        lol.append(entry)
    print(lol)


if __name__ == '__main__':
    list_of_lists(histogram(get_word_list()))

# DICTIONARY HISTOGRAM
# Something is wrong?

# READ from this FILE
def get_word_list(file_name = '../sample_text.txt'):
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

    return words

# HISTOGRAM FUNCTION
def dict_histogram(list):
    '''
    Returns unique values and the
    number of occurances of each
    '''
    hist_dict = {}
    for word in list:
        if word not in hist_dict:
            hist_dict[word] = 1
        else:
            hist_dict[word] += 1

    print(hist_dict)
    return hist_dict


if __name__ == '__main__':
    dict_histogram(get_word_list())

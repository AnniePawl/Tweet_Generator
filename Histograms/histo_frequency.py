# FREQUENCY HISTOGRAM
# Returns the number of times that a specified word appears in a file

# Results should look like: 'narwhal 5'

# READ FROM THIS FILE
# file = open("../sample_text.txt")
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

# FREQUENCY FUNCTION
def frequency(word, list):
    '''
    Returns the number of times
    a specified word appears in
    a file '''
    
    print(word, list[word])

if __name__ =='__main__':
    frequency('narwhal', histogram(get_word_list()))
    frequency('and', histogram(get_word_list()))
    frequency('white', histogram(get_word_list()))

# LIST OF COUNTS

# Results should look like this:
''' counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])] '''

# READ from this FILE
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

    return words

# LIST OF COUNTS HISTOGRAM
def counts_list(words):

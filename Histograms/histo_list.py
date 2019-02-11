# LISTS OF LISTS
# Two-dimensional arrays

# Results should look like this:
''' histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]] '''

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

    return words

# LIST OF LISTS HISTOGRAM
def list_of_lists_hist(list_of_words):
    lol = []

    for word in list_of_words:
        word_found = False
        for baby_list in lol:
            if baby_list[0] == word:
                # print("here")
                baby_list[1] += 1
                word_found = True

        if not word_found:
            lol.append([word, 1])

    print(lol)
    return lol

def histo_storage(self, file):
    '''writes results to file'''

if __name__ == '__main__':
    list_of_lists_hist(get_word_list())

# LISTS OF LISTS
"""
Results should look like this:</br>
histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
"""

# READ from this FILE
# file = open("../words.txt")

# READ FROM THIS FILE
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


def list_of_lists_hist(list_of_words):
    lol = []

    for word in list_of_words:
        word_found = False
        for baby_list in lol:
            if baby_list[0] == word:
                print("HERE")
                baby_list[1] += 1
                word_found = True

        if not word_found:
            lol.append([word, 1])

    print(lol)
    return lol


if __name__ == '__main__':
    list_of_lists_hist(get_word_list())

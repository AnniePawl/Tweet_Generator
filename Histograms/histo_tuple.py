# TUPLE HISTOGRAM
# Tuple is a sequence of Immutable objects

# Results should look like this:
''' histogram = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)] '''


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


# TUPLE HISTOGRAM
def list_of_tuples_hist(list_of_words):
    lot = []

    for word in list_of_words:
        word_found = False
        for baby_tuple in lot:
            if baby_tuple[0] == word:
                current_count = baby_tuple[1]
                lot.remove(baby_tuple)
                lot.append((word, current_count + 1))
                word_found = True

        if not word_found:
            lot.append((word, 1))

    print(lot)
    return lot

if __name__ == '__main__':
    list_of_tuples_hist(get_word_list())

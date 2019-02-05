# LISTS OF LISTS
```Results should look like this:</br>
histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
```

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

# Another option?
for word in word_list:
    found = False
    for inner_list in list:
        if word == inner_list[0]:
            inner_list[1] += 1
            found = True
            break
        if not found:
            list.append([word,1])

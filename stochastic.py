# SIMPLE STOCHASTIC SAMPLING
import random

phrase = "one fish two fish red fish blue fish"
phrase_list = phrase.split()
# print(phrase_list)

def histogram(phrase_list):
    '''
    Returns unique values and the
    number of occurances of each
    '''
    dict = {}
    for word in phrase_list:
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
    return(lol)


# PROBABILITY Function
def Stochastic(lol):
    word_frequency = 0
    cum_prob = 0.0

    for item in lol:
        word_frequency += item[1]

    random_num =  random.uniform(0, 1)
    for value in phrase_list:
        cum_prob += value[1]/word_frequency


# # TESTING THE WATERS
# def test_probability(phrase_list):
#     count= dict(phrase_list)
#     for item in histogram:
#         count[item[0]] = 0
#
#     for i in range(0, 100):
#         count[histogram(phrase_list)] += 1
#
#     print(count)

if __name__ == '__main__':
    dictionary = histogram(phrase_list)
    print(dictionary)
    lol2 = list_of_lists(dictionary)
    print(dict)
    Stochastic(lol2)

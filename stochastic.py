# SIMPLE STOCHASTIC SAMPLING SITUATION
    # Sample Words by Frequency
    # Test Relative Probabilities

import random

# CREATE a DICTIONARY of WORDS
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


# CREATE A PROBABILITY DICTIONARY
def probability_dict(hist_dict):
  ''' Takes a histogram dictionary
  and returns a probability dictionary '''
  total_counts = 0.0
  for word in hist_dict:
    total_counts += hist_dict[word]

  prob_dict = {}
  ''' probability = number of occurances / total words '''
  for word in hist_dict:
    prob_dict[word] = hist_dict[word] / total_counts

  return prob_dict

# STOCHASTIC (RANDOM) SAMPLE FUNCTION
def stochastic_word(prob_dict):
  '''Takes a probability dictionary and
  randomly produces a word according to the given probabilities '''
  random_point = random.uniform(0, 1)
  cumulitive_probability = 0
  for word in prob_dict:
    cumulitive_probability += prob_dict[word]
    if cumulitive_probability > random_point:
      return(word)


# TEST FUNCTION
def test(prob_dict, num_generations=100):
    ''' iterates 100 times to test random sampling'''
    generations = [stochastic_word(prob_dict)for _ in range(num_generations)]
    # Get historgram for the generations.
    gen_hist = histogram(generations)
    gen_prob = probability_dict(gen_hist)

    print("COMPARISON: %s NUM TRIALS" % num_generations)
    print(prob_dict)
    print(gen_prob)

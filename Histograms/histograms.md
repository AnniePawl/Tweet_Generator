## Histograms
Programs must satisfy the following specifications: </br>
- A `histogram()` function which takes `source_text` arguments and returns histogram data structure that stores each unique word along with number of times word appears in text.
- A `unique_words()` function that takes histogram argument and returns total count of unique words in histogram
- A `frequency()` function that takes a `word` and `histogram` argument and returns number of times words appears in text. Ex, given the word `mystery` and the Holmes histogram, integer 20 returned

### Dictionary of key-value pairs
- *Coding Effort:* Easy (1 for loops)
- *Time Efficiency:* Fast, O(n)
- *Space Efficiency:*
```
histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
```

### List of Lists
- *Coding Effort* Medium-Easy (Double for loop)
- *Time Efficiency* Slower, O(n^2)
- *Space Efficiency* Efficient-ish, some wasted space
```
histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
```

### List of Tuples
- *Coding Effort* Medium-Hard (b/c immutable)
- *Time Efficiency* Slower, O(n^2)
- *Space Efficiency* Efficient! No wasted space
```
histogram = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
```

### List of Counts
- *Coding Effort*  Harder
- *Time Efficiency* Slower O(n^2)
- *Space Efficiency* Most efficient!

### Invert words and counts
```counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]
```

# Tweet Generator App Architecture
## Important Questions to Consider

### What are application's key features? Are they separated into their own files?
 - Users can generate a series of random words that are grammatically correct-ish from

### Are module, file, function, and variable names appropriate ? Would a new programmer be able to understand it ?

### What are scopes of variables? Are they appropriate to use case?

### Are functions small and clearly specified ?

### Are functions well organized in OOP style by defining them as methods of a class?

### Can files be used both as modules and scripts?

### Can modules be used independently or are they dependent ?  


## Example
A high-level architecture might look like this, with each file acting as both a module and a script.

app.py          # main script, uses other modules to generate sentences </br>
cleanup.py      # module for cleaning up source text </br>
tokenize.py     # module for creating lists of tokens from a text </br>
word_count.py   # module for generating histograms from a list of tokens </br>
sample.py       # module for generating a sample word from a histogram </br>
sentence.py     # module for generating a sentence from a histogram </br>

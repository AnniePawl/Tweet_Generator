# Tweet Generator App Architecture
## Important Questions to Consider
1. What are application's key features? Are they separated into their own files?

2. Are module, file, function, and variable names appropriate ? Would a new programmer be able to understand it ?

3. What are scopes of variables? Are they appropriate to use case?

4. Are functions small and clearly specified ?

5. Are functions well organized in OOP style by defining them as methods of a class?

6. Can files be used both as modules and scripts?

7. Can modules be used independently or are they dependent ?  


## Example
A high-level architecture might look like this, with each file acting as both a module and a script.
- **app.py**          # main script, uses other modules to generate sentences </br>
- **cleanup.py**      # module for cleaning up source text </br>
- **tokenize.py**     # module for creating lists of tokens from a text </br>
- **word_count.py**   # module for generating histograms from a list of tokens </br>
- **sample.py**       # module for generating a sample word from a histogram </br>
- **sentence.py**     # module for generating a sentence from a histogram </br>

# Modules
A module is a **python object** with arbitrarily named attributes that you can bind and reference. _A module can define functions, classes, and variables._ It can also include runnable code. Modules _can be imported into other modules._
</br>
</br>
For longer programs, it's convenient to prepare the input for the interpreter. You can put definitions into a file and use them in a script.

## Importing Modules
Import statements are executed in two steps:</br>
    - **Find a module**, and initialize if necessary </br>
    - **Define name(s)** in local namespace.
It's customary to place all import statements _at the beginning of a module or script_. Imported modules names are placed in the importing module's global symbol table.</br>
- *Symbol Tables:*
Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. The author of a module can use global variables in the module w/o worrying about accidental clashes with a user's global variables. </br>

There are variations of import statements.</br>
- Imports names from a module directly into the importing modules symbol table.`from fibo import fib, fib2`
- Imports _all_ names that a modules defines `from fibo import *`
- Name following 'as' is bound directly to imported module `import fibo as fib`

## Executing Module's as Scripts
When you run a Python module with `python fibo.py <arguments>` the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:

```if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

```$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

### Standard Modules
Python comes with a library of standard modules. Some are built into the interpreter and provide access to operations that are not part of the core language.

### runpy
A module used to locate and run python modules without importing them first.

### dir() Function
A built-in function that is _used to find out which names a module defines_

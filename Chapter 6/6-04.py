# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) 
# by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, 
# these new words and meanings should automatically be included in the output.

glossary = {
    'print':'it print messages',
    'list':'data collection',
    'string':'collection of characters',
    'int':'numbers with out decimal point',
    'float':'number with decimal point'
}

for key, value in glossary.items():
    print("\n")
    print(key)
    print(value)

glossary['strip'] = 'remove white space from both side of string'
glossary['lstrip'] = 'remove white space from left side of string'
glossary['rstrip'] = 'remove white space from right side of string'
glossary['range'] = 'create squance of the number'
glossary['append'] = 'add item in list'

for key, value in glossary.items():
    print("\n")
    print(key)
    print(value)
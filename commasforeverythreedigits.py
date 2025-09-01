Here is the code with added descriptive comments:

```python
# Import the regular expression module, which provides support for regular expressions in Python.
import re

# Compile a regular expression pattern to match US-style currency numbers (e.g. 1,234,567.89).
# The pattern breaks down as follows:
# ^        : Start of the string
# (\d){0,3}: Match 0 to 3 digits (the thousands separator is optional)
# (,(\d){3})*: Optionally match a comma followed by exactly 3 digits (the decimal part is not handled here)
# $        : End of the string
numRegex = re.compile(r'^((\d){0,3})((,(\d){3})*)$')

# Define a list of strings to test against the regular expression pattern.
strings_list = (
    '42',  # A simple integer
    '1,234',  # A number with a thousands separator
    '6,368,745',  # A number with multiple thousands separators
    '12,34,567',  # Another number with multiple thousands separators
    '1234')  # A number without a thousands separator

# Iterate over each string in the list.
for item in strings_list:
    # Search the current string for a match against the regular expression pattern.
    numfind = numRegex.search(item)
    
    # If a match was found, print the matched number.
    if numfind is not None:
        print(numfind.group())  # Print the matched number
```
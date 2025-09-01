# commasforeverythreedigits.py

**Regular Expression Validator**

This Python script uses regular expressions to validate and extract US-style currency numbers from a list of strings.

**Functionality**

The script performs the following tasks:

1. **Import the `re` module**: The script imports the `re` module, which provides support for regular expressions in Python.
2. **Compile a regular expression pattern**: The script compiles a regular expression pattern to match US-style currency numbers. The pattern consists of:
	* `^` : Start of the string
	* `(\d){0,3}` : Match 0 to 3 digits (the thousands separator is optional)
	* `(,(\d){3})*` : Optionally match a comma followed by exactly 3 digits (the decimal part is not handled here)
	* `$` : End of the string
3. **Define a list of test strings**: The script defines a list of strings to test against the regular expression pattern.
4. **Iterate
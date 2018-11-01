Introduction to the use of regular expressions in Python.

hello.py is a basic hello world program (not a script).

filter.py (21 March 2011) is a line-oriented script (not a program)
that filters standard input: it removes '\n' and '.' characters,
maps 'V' and 'v' to 'U' and 'u', and lower cases the string. Note
that it uses the String replace() method instead of the Regular
Expression sub() method.

demo.py (6 December 2016) is a word-oriented program that lower
cases a sample string, strips punctuation from it, and splits it
into an array. It then iterates through the array, using the Regular
Expression sub() method to map 'v' to 'u' and to map the substring
'us' at the end (but not in the middle) of a word to 'a'.


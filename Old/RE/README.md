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

Objectives discussed on Wednesday, March 13th

Challenge 1:
Suspensions
Change any vowels with macron over them to remove macron and append the character with an 'm'.
Example: Cōpare -> Compare
Tip: Use od -c compare.txt to learn code for macron.

Challenge 2:
Remove curly brackets and matain characters inside.
Example: {choco}late -> chocolate
May look something like: \{[a-z A-Z]+\}

Next Meeting: Friday, March 15th 10:00am-11:30am

Objectives discussed on Wednesday, March 20th

Challenge for Mr. Evans:
Macron
Find a way to match any character with a macron.

Challenges for Jordan:

One: Begin properly changing the spelling of words with macrons. Specifically, cō becomes con, and generally ō should become om. Tailor other substitutions to exceptions. Keep eue as eue.

Two: Create a sample program that takes any collection of characters fitting the pattern vowel, u|i, vowel to vowel, v or j (respectively),vowel.

Next Meeting: March 27th, 2019

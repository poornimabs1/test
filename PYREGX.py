#importing the Regular Expressions (regex) module.
# This module lets you search, match, extract, replace, and manipulate text patterns efficiently.

import re
from os.path import sep

text = "Test the string1 manipulation"
text2 = 'step1,step2:step3'
pattern1= "string1"
pattern2= "Test"
replacement= "string2"
sep=","

#1. searches for a pattern anywhere in the string and returns the first match it finds.
search = re.search(pattern1, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

#2. Match (Imp note re.match() checks whether a pattern matches at the beginning of a string.)
match = re.match(pattern2, text)
if match:
        print("Match found:", match.group())
else:
        print("Match not found")

#3. Replace
new_txt = re.sub(pattern1, replacement, text)
print(new_txt)

#4.In Python, both split() and re.split() are used to break a string into parts.
# but they differ in power, flexibility, and use cases.

txtspl = re.split(sep, text2)
print(txtspl)
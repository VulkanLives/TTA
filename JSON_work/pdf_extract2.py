import re
from tkinter import StringVar

from pdfminer.high_level import extract_pages, extract_text

a= type
#extract text
text = extract_pages("750 firestorm 2.pdf")
print(text)

#lfind anything that starts with a lowercase or an uppercase character at least
# one of those and then is followed by a comma exactly one comma
# uh and then followed by a space exactly one space so this is a regular
# expression we say any letter that is uppercase or lowercase at least one
# but as many as we want followed by oneby exactly one comma and followed by exactly one space
#pattern = re.compile(r"[a-zA-Z] + ,{1}\s{1}")
#match = pattern.findall(str(text))

bold_pattern = r'\*\*(.*?)\*\*'
pattern = re.compile(r'\*\*(.*?)\*\*')   # pattern for finding all words 9n bold
# does not work, need try and look for capitalised word that brackets after them
#https://edoras.sdsu.edu/doc/nedit-5.5-rp/parenConstructs.html
match = re.findall(pattern=bold_pattern, string=a)
flag_match = re.findall(pattern=bold_pattern, string=a, flags=re.DOTALL)

print("match ="+ str(match))
print(flag_match) # using the flag

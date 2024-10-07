import json
import re

import pandas as pd
from pdfminer.high_level import extract_pages



df = pd.read_json('../Salamander_Firestorm _750pts.json')
#print(df)
json_column = df['roster']
#print(json_column)

extracted_data: [] = json_column['forces']
print("extracted data = " +str(extracted_data))

#write raw text to file, for debug purpses really
with open("Output.txt", "w") as text_file:
    text_file.write(str(extracted_data))

text = extract_pages("Output.txt")
#pattern rules looking for text in between "{ }" brackets
pattern_rule = re.search(r"\[({A-Za-z0-9_}+)\]", str(text))
print(pattern_rule)
#with open("extract.txt", "w") as text_file:
 #   text_file.write(str(pattern_rule))

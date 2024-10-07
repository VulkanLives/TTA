import json
import pandas as pd

from JSON_work import army_class

with open('../Salamander_Firestorm _750pts.json', 'r') as file:
    data = json.load(file)
df_read_json = pd.read_json(json.dumps(data), orient='index')
print("DataFrame using pd.read_json() method:")
print(df_read_json.columns)
data_array = []
#print("column = "+str(df_read_json[0]))
print(df_read_json.head())
#print(df_read_json.loc[:,"Grades"])

army_class.Army(data)

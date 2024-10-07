import json
import pandas as pd
import numpy as np

army_array = ["",""]
class Army():
    array2 = np.array(11)
    #army = ['costs', 'costLimits', 'forces', 'id', 'name', 'battleScribeVersion',
     #      'generatedBy', 'gameSystemId', 'gameSystemName', 'gameSystemRevision',
      #     'xmlns']
    x=0
    ################################
    f= open('../Salamander_Firestorm _750pts.json')
    data = json.load(f)
    
    
    for i in data["roster"]:
        print(i)

    df = pd.DataFrame(data)
    print(df)
    df_read_json = pd.read_json(json.dumps(data), orient='index')
    print("DataFrame using pd.read_json() method:")
    print(df_read_json.values)
    print(df_read_json)
    #army_array.append(df_read_json)
    print("df read cols " +str(df_read_json.columns.__len__()))
    print("df read cols " +str(df_read_json.columns))
    y= int(df_read_json.columns.__len__())
    
    
    for x in range (y):
        army_array.append(int(df_read_json.columns[x]))
        x+=1

print(str(army_array))
    
army = Army()
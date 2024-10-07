import pandas as pd
import json

data = {
    "One": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Two": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    }
}

# Corrected the attribute name to dumps
df_read_json = pd.read_json(json.dumps(data), orient='index')
print("DataFrame using pd.read_json() method:")
print(df_read_json)

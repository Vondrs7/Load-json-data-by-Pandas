import pandas as pd
import json

# used pandas library
# used "with" for open, read and close json file
# loaded to "data" variable
with open("configClear_v2.json") as f:
    data = json.load(f)

# separate BDI part from json file
data = data["frinx-uniconfig-topology:configuration"]
data_cisco = data["Cisco-IOS-XE-native:native"]
data_interface = data_cisco["interface"]
data_bdi = data_interface["BDI"]
data_ = data_bdi[0]

# input pandas frame to variabe 
df = pd.DataFrame(data_)


print(df)








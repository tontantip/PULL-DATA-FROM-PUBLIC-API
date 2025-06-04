## import library requests and pprint
import requests
from pprint import pprint

## set path API
url = "https://exat-man.web.app/api/EXAT_Accident/2568/01"
## GET API
data = requests.get(url)
## print all_result
result = data.json()
all_result = result["result"]
print(f"Count {len(all_result)}") ## number of list is 51 
pprint(all_result[51]) ## data number 51 (last data)


## create list of data 
id = []
accident_date =[]
accident_time = []
cause = []
dead_femel=[]
dead_man =[]
expw_step =[]
injur_femel = []
injur_man = []
weather_state =[]

## append data from each all_data to list of data
for i in all_result:
    _accident_date = i["accident_date"]
    _id = i["_id"]
    _accident_time = i["accident_time"]
    _cause = i["cause"]
    _dead_femel = i["dead_femel"]
    _dead_man = i["dead_man"]
    _expw_step = i["expw_step"]
    _injur_femel = i["injur_femel"]
    _injur_man = i["injur_man"]
    _wearther = i["weather_state"]
    id.append(_id)
    accident_date.append(_accident_date)
    accident_time.append(_accident_time)
    cause.append(_cause)
    dead_femel.append(_dead_femel)
    dead_man.append(_dead_man)
    expw_step.append(_expw_step)
    injur_femel.append(_injur_femel)
    injur_man.append(_injur_man)
    weather_state.append(_wearther)

## import pandas
import pandas as pd
## create data frame
df = pd.DataFrame({
    "id": id,
    "accident_date": accident_date,
    "accident_time": accident_time,
    "cause":cause,
    "dead_man":dead_man,
    "dead_femel":dead_femel,
    "injur_man":injur_man,
    "injur_femel":injur_femel,
    "place":expw_step,
    "weather":weather_state
})
## print data frame
print(df)

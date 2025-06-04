## import requests and pprint
import requests
from pprint import pprint
## set url API
url = "https://data.tmd.go.th/api/DailySeismicEvent/v1/?uid=api&ukey=api12345&format=json"
data = requests.get(url)
if data.status_code == 200:
    daily = data.json()
    result = daily['DailyEarthquakes']
    print("request API OK")
else:
    print("API ERROR)

import pandas as pd
df = pd.json_normalize(result)
df

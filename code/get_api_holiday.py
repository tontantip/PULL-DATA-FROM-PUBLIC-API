## import request and pprint
import requests
from pprint import pprint
## set country to request API GB: united kingdom, US: United state, CN: china
country = ["GB","US","CN"]
## set list lst_data for collect data
lst_data = []
## for loop request API each country in year 2025
for i in country:
    year = 2025
    url= f'https://date.nager.at/api/v3/publicholidays/{year}/{i}'
    data = requests.get(url)
    if data.status_code ==200:
        result = data.json()
        for j in result:
            lst_data.append(j)
    else:
        print("API ERROR")

  ## set list of data 
_counties = []
_countryCode = []
_date = []
_fixed = []
_global = []
_launchYear = []
_name = []
_types = []

## for loop data from lst_data
for k in range(len(lst_data)):
    i = lst_data[k]
    ## append data to each list of data
    _counties.append(i["counties"])
    _countryCode.append(i["countryCode"])
    _date.append(i['date'])
    _fixed.append(i['fixed'])
    _global.append(i['global'])
    _name.append(i['name'])
    _launchYear.append(i['launchYear'])
    _types.append(i['types'])

## import pandas
import pandas as pd
df = pd.DataFrame({
 'counties' : _counties,
 'countryCode': _countryCode,
 'date' : _date,
 'fixed' :_fixed,
 'global' : _global, 
 'launchYear' : _launchYear, 
 'name' : _name,
 'types' : _types
})
## print data frame
df

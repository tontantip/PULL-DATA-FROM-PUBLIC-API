## import request and pprint
import requests
from pprint import pprint
## set year list 2019-2024
year = ["2019-01-01","2020-01-01","2021-01-01","2022-01-01","2023-01-01","2024-01-01"] 
## set list result for collect data from API
result = []
## for loop request API each year (2019-2024)
for i in year:
    url = f"https://dataservices.mof.go.th/api/data/importexport/get_data_overview?from={i}"
    data = requests.get(url)
    if data.status_code == 200:
        all = data.json()
        item = all['items']
        ## for loop append data for API to result list
        for k in item:
            result.append(k)
        print("OK")
    else:
        print("API ERROR")


## import pandas
import pandas as pd
## create data frame from list result
df = pd.json_normalize(result)
## rename head columns to thai (eazy to understand)
df_new = df.rename(columns = {
    "year_month": "ปี-เดือน ตามความถี่ในรูปแบบ Y-m-d",
    "import_baht" : "Import มูลค่า(บาท)",
    "import_us" : "Import มูลค่า(US$)",
    "import_rate" : "อัตราแลกเปลี่ยนนำเข้า",
    "export_baht" : "Export มูลค่า(บาท)",
    "export_us": "Export มูลค่า(US$)",
    "export_rate": "อัตราแลกเปลี่ยนส่งออก",
    "re_export_baht": "Re-Export มูลค่า(บาท)",
    "re_export_us" : "Re-Export มูลค่า(US$)",
    "tot_export_baht" : "Total Export",
    "tot_export_us" : "Total",
    "balance_baht":"ดุลการค้า มูลค่า(บาท)",
    "balance_us":"ดุลการค้า มูลค่า(US$)",
    "balance_percent":"ดุลการค้า เพิ่มลด %",
    "year_month_th":"ปี-เดือน ภาษาไทย"})
## print data frame
df_new
